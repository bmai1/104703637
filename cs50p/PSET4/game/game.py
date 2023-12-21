import random


# input positive integer for level
while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level > 0:
        break
# n is random number between 1 and level
if level == 1:
    n = 1
else:
    n = random.randrange(1, level)

# guess inputs
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > 0 and guess <= level:
        if guess > n:
            print("Too large!")
        if guess < n:
            print("Too small!")
        if guess == n:
            print("Just right!")
            exit()
    else:
        continue
