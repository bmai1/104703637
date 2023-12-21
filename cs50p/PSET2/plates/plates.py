def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # length between 2 and 6
    if len(plate) >= 2 and len(plate) <= 6:
        # all letters
        if plate.isalpha():
            return True

        # contains only num and letter (alphanumeric)
        if plate.isalnum():
            # first two characters are letters
            if plate[0:2].isalpha():
                # find first number
                for i in range(len(plate)):
                    if plate[i].isdigit():
                        # weird way to check first num is not 0
                        if str(plate[i]) != "0":
                            # num to end has no letters
                            if plate[i: len(plate) - 1].isdigit():
                                return True
    return False


main()

