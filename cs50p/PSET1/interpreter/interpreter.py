def main():
    equation = input("> ")
    # i think this is kind of hackish/unsafe
    print(float(eval(equation)))

    # this can't handle x and y values >10 however
    alternative_function = """
    def solve(equation):
    # convert first and second number to floats
    x = float(equation[0])
    y = float(equation[4])
    # determine operator using pattern matching
    match equation[2]:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y """


main()