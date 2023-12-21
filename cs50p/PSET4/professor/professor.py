from random import randint

def main():
    level = get_level()
    # two lists of 10 random numbers with level amount of digits
    xlist = []
    ylist = []
    score = 0
    for i in range(10):
        x = generate_integer(level)
        xlist.append(x)

        y = generate_integer(level)
        ylist.append(y)

        # print equation and set sum
        print(f"{xlist[i]} + {ylist[i]} = ", end="")
        sum = xlist[i] + ylist[i]

        # 3 guesses otherwise give answer and move on
        for j in range(3):
            try:
                guess = int(input())
            except ValueError:
                continue
            except EOFError:
                print("")
                exit()
            if guess == sum:
                score += 1
                break
            else:
                if j == 2:
                    print(f"{xlist[i]} + {ylist[i]} = {sum}")
                    break
                else:
                    print("EEE")
                    print(f"{xlist[i]} + {ylist[i]} = ", end="")
    print(score)

# ask for level input until 1, 2, or 3
def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        if n == 1 or n == 2 or n == 3:
            return n


# generate random integers with level digits
def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()