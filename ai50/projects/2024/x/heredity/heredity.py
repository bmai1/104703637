import csv
import itertools
import sys

PROBS = {
    # Unconditional probabilities for having gene
    "gene": {2: 0.01, 1: 0.03, 0: 0.96},
    "trait": {
        # Probability of trait given two copies of gene
        2: {True: 0.65, False: 0.35},
        # Probability of trait given one copy of gene
        1: {True: 0.56, False: 0.44},
        # Probability of trait given no gene
        0: {True: 0.01, False: 0.99},
    },
    # Mutation probability
    "mutation": 0.01,
}


def main():
    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):
        # Check if current set of people violates known information
        fails_evidence = any(
            (
                people[person]["trait"] is not None 
                and people[person]["trait"] != (person in have_trait)
            )
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}: ")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}: ")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p: .4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (
                    True 
                    if row["trait"] == "1" 
                    else False 
                    if row["trait"] == "0" 
                    else None
                ),
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) 
        for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    joint_p = 1

    for person, parents in people.items():
        # handle parents based on uncondtional probability
        if parents["mother"] is None and parents["father"] is None:
            if person in one_gene:
                gene = 1
            elif person in two_genes:
                gene = 2
            else:
                gene = 0

            trait = True if person in have_trait else False

            # probability of parent having specific genes and trait combination
            
            joint_p *= PROBS["gene"][gene] * PROBS["trait"][gene][trait]
        
        # genes dependent on parents
        else:
            mother = parents["mother"]
            father = parents["father"]

            # 2 genes = pass, 1 gene = 0.5 pass, 0 gene = no pass
            # mutation flips result

            if mother in two_genes:
                mother_pass = 1 - PROBS["mutation"]
            elif mother in one_gene:
                # 0.5 chance to pass, times chance to not mutate (into fail)
                # 0.5 chance to fail, times chance to mutate (into pass)
                mother_pass = 0.5 * (1 - PROBS["mutation"])
                mother_pass += 0.5 * PROBS["mutation"]
            else:
                mother_pass = PROBS["mutation"]

            if father in two_genes:
                father_pass = 1 - PROBS["mutation"]
            elif father in one_gene:
                father_pass = 0.5 * (1 - PROBS["mutation"])
                father_pass += 0.5 * PROBS["mutation"]
            else:
                father_pass = PROBS["mutation"]
            
            if person in two_genes:
                # both mother and father pass gene
                joint_p *= mother_pass * father_pass
                gene = 2

            elif person in one_gene:
                # either mother pass, father doesn't or father pass, mother doesn't
                not_mother_pass = 1 - mother_pass
                not_father_pass = 1 - father_pass
                joint_p *= not_mother_pass * father_pass + not_father_pass * mother_pass
                gene = 1

            else:
                # neither mother nor father pass
                joint_p *= (1 - mother_pass) * (1 - father_pass)
                gene = 0
            
            # probability of child having trait
            trait = True if person in have_trait else False
            joint_p *= PROBS["trait"][gene][trait]

    # print(joint_p)
    return joint_p


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        gene = 0
        if person in one_gene:
            gene = 1
        elif person in two_genes:
            gene = 2

        trait = True if person in have_trait else False

        probabilities[person]["gene"][gene] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # loop through person dicts, not person string names
    for person in probabilities:
        g = probabilities[person]["gene"]
        t = probabilities[person]["trait"]

        gene_sum = g[2] + g[1] + g[0]
        trait_sum = t[True] + t[False]
        
        for i in range(len(g)):
            probabilities[person]["gene"][i] /= gene_sum

        for i in range(len(t)):
            probabilities[person]["trait"][i] /= trait_sum


if __name__ == "__main__":
    main()
