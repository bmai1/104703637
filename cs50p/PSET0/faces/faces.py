txt = input()
for i in range(len(txt)):
    if txt[i] == ":":
        if txt[i + 1] == ")":
            # unicode for smile emoji, + converted to 000
            print("\U0001F642", end='')
        if txt[i + 1] == "(":
            # unicode for frown emoji
            print("\U0001F641", end='')
    else:
        if txt[i] != ")" and txt[i] != "(":
            print(txt[i], end='')
print("")
