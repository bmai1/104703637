def main():
    txt = input("Input: ")
    print(vowels(txt))


def vowels(txt):
    txt2 = ""
    # iterate through text finding vowels
    for i in range(len(txt)):
        letter = txt[i].lower()
        # check that letter is not vowel
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
            txt2 += txt[i]
    return txt2


main()