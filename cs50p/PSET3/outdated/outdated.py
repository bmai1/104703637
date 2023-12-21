def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date: ")
            # remove whitespace in 00/00/0000 format
            if date[0].isalpha() == False:
                date = date.strip()
            # split 00/00/0000 format
            split = date.split("/", 3)
            # split January 1, 0000 format
            split2 = date.split(" ", 3)
        except ValueError:
            continue
        # if first index of split is number and month is between 1-12, day between 1-31
        if (split[0].isdigit() and 0 < int(split[0]) <= 12 and 0 < int(split[1]) <= 31):
            break
        # if first index of split is month and day is between 1-31
        elif (split2[0].isalpha() and 0 < int(split2[1].replace(",", "")) <= 31):
            if "," in split2[1]:
                break

    # 00/00/0000 format
    if split[0].isdigit():
        for i in range(2):
            # add 0 in front if 1 digit day or month
            if int(split[i]) < 10:
                split[i] = "0" + split[i]
        # print year, month, day
        print(split[2] + f"-{split[0]}-" + split[1])

    # January 1, 0000 format
    if split2[0].isalpha():
        # find month number from list of months
        for i in range(12):
            if split2[0] == months[i]:
                num = str(i + 1)
        # add 0 in front if 1 digit day
        if int(num) < 10:
            num = "0" + num
        if int(split2[1].replace(",", "")) < 10:
            split2[1] = "0" + split2[1]
        # print year, month, day (without the comma)
        print(split2[2] + f"-{num}-" + split2[1].replace(",", "") )


main()