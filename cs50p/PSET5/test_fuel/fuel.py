def main():
    while True:
        try:
            fraction = input("> ")
            f = convert(fraction);
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        except NameError:
            continue
        # check fraction less then one and is valid
        if check(fraction) == True:
            break

    print(f'{f}%')


def convert(fraction):
    if not fraction[0].isdigit() or not fraction[2].isdigit():
        raise ValueError("X and Y need to be integers")
    if fraction[2] == '0':
        raise ZeroDivisionError("Divide by Zero")
    if int(fraction[0]) > int(fraction[2]):
        raise ValueError("X greater than Y")
    return int(round(100 * eval(fraction)))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + '%'


# check no decimals or other operators
def check(fraction):
    for i in range(len(fraction)):
        if fraction[i] == "." or fraction[i] == "+" or fraction[i] == "-" or fraction[i] == "*":
            return False
    return True


if __name__ == "__main__":
    main()