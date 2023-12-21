from random import randint


secret_number = str(randint(0,99999)).zfill(5)
n = len(secret_number)
g = " "
def main():
    # generate random number between 0000-9999
    global secret_number
    while True:
        try:
            setGuess()
            guessValidator(g)
        except ValueError:
            continue
        if g == secret_number:
            exit("You win!")
        else:
            print(hint(g))


def setGuess():
    global n
    global g
    g = input("Guess: ").strip()


def guessValidator(guess):
    if not guess.isdigit():
        raise ValueError("Invalid guess")
    if len(guess) != n:
        raise ValueError("Invalid guess length")


def hint(guess):
    global secret_number
    global n
    s = [0 for i in range(10)]
    g = [0 for i in range(10)]

    # digit in right place
    correct = 0
    # digit occurence within secret number
    within = 0

    # correct digits in correct index/location
    for i in range(n):
        if secret_number[i] == guess:
            correct += 1
        else:
            s[int(secret_number[i])] += 1
            g[int(guess[i])] += 1

    # count correct digits with wrong index
    for j in range(10):
        if s[j] == g[j]:
            within += g[j]
        elif s[j] > g[j]:
            within += g[j]
        else:
            within += s[j]

    return str(correct) + 'A' + str(within) + 'B'


if __name__ == "__main__":
    main()