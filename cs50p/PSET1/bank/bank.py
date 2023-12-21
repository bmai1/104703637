def main():
    greeting = input("> ").strip().lower()
    print(check(greeting))


def check(greeting):
    # first five characters == hello
    if greeting[0:5] == "hello":
        return "$0"
    # first letter == h
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


main()