def main():
    # if you leave input here empty, then check50 will say code is not asking for input at all
    txt = input("> ").lower().strip()
    # input is a string
    if txt == "42" or txt == "forty-two" or txt == "forty two":
        print("Yes")
    else:
        print("No")

main()