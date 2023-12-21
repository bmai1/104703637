def main():
    time = input("What time is it? ")
    # prints nothing if time doesn't fit
    if not convert(time):
        exit()
    print(convert(time) + " time")


def convert(time):
    # input is str
    for i in range(len(time)):
        if time[i] == ":":
            # hour variable depending on colon
            hour = int(time[0:i])
            if hour >= 7 and hour <= 8:
                return "breakfast"
            elif hour >= 12 and hour <= 13:
                return "lunch"
            elif hour >= 18 and hour <= 19:
                return "dinner"
    # 12hr check var, must be in [#:## #.m] format or it will not work
    check12 = time[len(time) - 3 : len(time)]
    # if a.m and between 7 and 8, return breakfast
    if check12 == "a.m":
        hour = int(time[0])
        if hour >= 7 and hour <= 8:
            return "breakfast"
    elif check12 == "p.m":
        if time[0:2] == "12" or (time == "1:00 p.m"):
            return "lunch"
        elif (time[0] == 6) or (time == "7:00 p.m"):
            return "dinner"


if __name__ == "__main__":
    main()