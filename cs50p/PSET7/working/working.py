import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9 AM to 5 PM
    format1 = r"^(([1-9]|1[0-2]) (AM|PM) to ([1-9]|1[0-2]) (AM|PM))"
    # 9:00 AM to 5:00 PM
    format2 = r"^(([1-9]|1[0-2]):[0-5][0-9] (AM|PM) to ([1-9]|1[0-2]):[0-5][0-9] (AM|PM))"

    if not re.match(format1, s) and not re.match(format2, s):
        raise ValueError("Invalid input.")

    if re.match(format1, s):
        am_hours = re.search(r"([1-9]|1[0-2]) AM", s)
        am_hours = am_hours.group()
        if am_hours[1] == ' ':
            am_hours = '0' + am_hours[0] + ":00"
        elif am_hours[0:2] != "12":
            am_hours = am_hours[0:2] + ":00"
        if am_hours[0:2] == "12":
            am_hours = "00:00"

        pm_hours = re.search(r"([1-9]|1[0-2]) PM", s)
        pm_hours =  pm_hours.group()
        if pm_hours[1] == ' ':
            pm_hours = str(12 + int(pm_hours[0])) + ":00"
        elif pm_hours[0:2] != "12":
            pm_hours = str(12 + int(pm_hours[0:2])) + ":00"
        if pm_hours[0:2] == "12":
            pm_hours = "12:00"


    elif re.match(format2, s):
        am_hours = re.search(r"([1-9]|1[0-2]):[0-5][0-9]+? AM", s)
        am_hours = am_hours.group()
        if am_hours[1] == ':':
            am_hours = '0' + am_hours[0] + am_hours[1:4]
        elif am_hours[0:2] != "12":
            am_hours = am_hours[0:5]

        if am_hours[0:2] == "12":
            am_hours = "00" + am_hours[2:5]


        pm_hours = re.search(r"([1-9]|1[0-2]):[0-5][0-9]+? PM", s)
        pm_hours = pm_hours.group()
        if pm_hours[1] == ':':
            pm_hours = str(12 + int(pm_hours[0])) + pm_hours[1:4]
        elif pm_hours[0:2] != "12":
            pm_hours = str(12 + int(pm_hours[0:2])) + pm_hours[2:5]
        if pm_hours[0:2] == "12":
            pm_hours = "12:00"


    for c in s:
        # check if AM or PM comes first
        if c == 'A':
            return am_hours + " to " + pm_hours
        elif c == 'P':
            return pm_hours + " to " + am_hours





if __name__ == "__main__":
    main()