def main():
    while True:
        try:
            prompt = input("> ")
            fraction = eval(prompt)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        except NameError:
            continue
        # check fraction less then one and is valid
        if fraction <= 1 and check(prompt) == True and prompt[0].isdigit():
            break

    if fraction < 0.1:
        print("E")
        exit()
    if fraction >= 0.99:
        print("F")
        exit()
    print(str(int(round(100 * fraction))) + "%")


# check no decimals or other operators
def check(prompt):
    for i in range(len(prompt)):
        if prompt[i] == "." or prompt[i] == "+" or prompt[i] == "-" or prompt[i] == "*":
            return False
    return True


main()