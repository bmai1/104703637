def main():
    txt = input()
    print(shorten(txt))


def shorten(word):
    # remove vowels using translate
    no_vowels = word.maketrans(dict.fromkeys('aeiouAEIOU'))
    return word.translate(no_vowels)


if __name__ == "__main__":
    main()