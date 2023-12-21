def main():
    # array of names
    names = []
    while True:
        try:
            # add names to array
            name = input("Name: ")
            names.append(name)
        except EOFError:
            # newline
            print("")
            # add "and" to last name in array if more than 1 name
            if len(names) > 1:
                names[-1] = "and " + names[-1]
            print("Adieu, adieu, to ", end="")
            # commas if 3+ names
            if len(names) > 2:
                print(", ".join(names))
            else:
                print(" ".join(names))
            exit()
main()