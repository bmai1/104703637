import re


def main():
    print(count(input("Text: ")))


def count(s):
    if s.strip() == "um" or s.strip() == "Um":
        return 1
    return len(re.findall(r"\A(u|U)m\W", s)) + len(re.findall(r"\W(u|U)m\W", s)) + len(re.findall(r"\W(u|U)m\Z", s))


if __name__ == "__main__":
    main()