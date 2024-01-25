# python3 generate.py data/structure0.txt data/words0.txt output.png
import sys

from crossword import *


class CrosswordCreator():
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        for var, possible_words in self.domains.items():
            rm = []
            for word in possible_words:
                if len(word) != var.length:
                    rm.append(word)

            # remove words with different length from variable
            for word in rm:
                self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        # no intersection implies arc consistency
        if self.crossword.overlaps[x, y] == None:
            return False

        i, j = self.crossword.overlaps[x, y]

        # should revert to set
        domain_x = list(self.domains[x])

        # words to remove
        rm = [word_x for word_x in domain_x if all(word_x[i] != word_y[j] for word_y in self.domains[y])]

        self.domains[x] = {word_x for word_x in self.domains[x] if word_x not in rm}

        return len(rm) != 0

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        # arcs are variables that overlap
        if arcs == None:
            arcs = []
            v = self.crossword.variables
            for x in v:
                for y in v:
                    if x == y:
                        continue
                    if self.crossword.overlaps[x, y] != None:
                        arcs.append((x, y))

        while len(arcs) != 0:
            # dequeue (remove front and return value)
            x, y = arcs.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                # for each Z in X.neighbors - {Y}:
                for z in self.crossword.neighbors(x) - {y}:
                    arcs.append((z, x))

        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        return len(assignment) == len(self.crossword.variables)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        words = []
        for var, val in assignment.items():
            # skip if assignment not complete
            if val == None:
                continue

            if var.length != len(val) or val in words:
                return False
            words.append(val)

            if var.length != len(val):
                return False

            neighbors = self.crossword.neighbors(var)
            for n in neighbors:
                if self.crossword.overlaps[var, n] != None:
                    i, j = self.crossword.overlaps[var, n]
                    # see if conflict with assignment of neighbors
                    # check if neighbor in assignment because it can be imcomplete
                    if n in assignment and val[i] != assignment[n][j]:
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # least-constraining values
        lcv = {val: 0 for val in self.domains[var]}
        neighbors = self.crossword.neighbors(var)

        for word_x in self.domains[var]:
            # neighbor variables
            for n in neighbors:
                if n not in assignment and self.crossword.overlaps[var, n] != None:
                    i, j = self.crossword.overlaps[var, n]
                    # count number of words ruled out
                    for word_y in self.domains[n]:
                        if word_x[i] != word_y[j]:
                            lcv[word_x] += 1

        # sort key (variable word values) based on lcv
        return sorted(lcv, key=lambda x: lcv[x])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned = None
        # minimum remaining values in domain
        mrv = float('inf')

        for var in self.crossword.variables:
            if var not in assignment:
                if len(self.domains[var]) < mrv:
                    mrv = len(self.domains[var])
                    unassigned = var
                elif len(self.domains[var]) == mrv:
                    # compare degrees (number of neighbors), use higher
                    d1 = len(self.crossword.neighbors(unassigned))
                    d2 = len(self.crossword.neighbors(var))

                    if d1 < d2:
                        unassigned = var

        return unassigned

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if len(assignment) == len(self.crossword.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for val in self.domains[var]:
            assignment[var] = val
            if self.consistent(assignment):
                res = self.backtrack(assignment)
                if len(res) == len(self.crossword.variables):
                    return res
                assignment[var] = None

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
