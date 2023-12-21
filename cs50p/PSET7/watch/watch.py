import re


def main():
    print(parse(input("HTML string: ")))


def parse(s):
    r = re.search(r'embed.+?"', s)
    if r == None:
        return None
    # from embed/ to end quote
    embed = s[r.span()[0]:r.span()[1]]
    url = embed[6:len(embed) - 1]
    return "https://youtu.be/" + url


if __name__ == "__main__":
    main()