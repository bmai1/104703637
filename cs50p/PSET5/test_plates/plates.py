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
        # num lock
        lock = False
        # alphanumeric and first two are letters
        if plate.isalnum() and plate[0:2].isalpha():
            for c in plate:
                if c.isdigit():
                    if lock == False and c == '0':
                        return False
                    lock = True
                if lock == True and not c.isdigit():
                    return False
            return True
    return False


if __name__ == "__main__":
    main()