import re
from datetime import date
# from num2words import num2words


def main():
    dob = input("Date of Birth: ")
    validateDob(dob)
    print(num2words(toMinutes(dob)).capitalize().strip() + " minutes")


# num2words module doesn't work, so manual implementation.
def num2words(num):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
            'eighteen', 'nineteen']

    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']

    if num < 20:
        return ones[num]
    if num < 100:
        return tens[num // 10 - 2] + ('-' + ones[num % 10] if num % 10 > 0 else '')
    if num < 1000:
        return ones[num // 100] + ' hundred ' + (num2words(num % 100) if num % 100 > 0 else '')
    if num < 1000000:
        return num2words(num // 1000) + ' thousand, ' + (num2words(num % 1000) if num % 1000 > 0 else '')
    if num < 1000000000:
        return num2words(num // 1000000) + ' million, ' + (num2words(num % 1000000) if num % 1000000 > 0 else '')


def validateDob(dob):
    # MM-DD-YYYY regEx
    date_regex = r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    if not re.match(date_regex, dob):
        exit("Invalid")


def toMinutes(dob):
    bday = date.fromisoformat(dob)
    delta = date.today() - bday
    return delta.days * 1440

    # # map months
    # months = {
    #    "Jan": 1,
    #    "Feb": 2,
    #    "Mar": 3,
    #    "Apr": 4,
    #    "May": 5,
    #    "Jun": 6,
    #    "Jul": 7,
    #    "Aug": 8,
    #    "Sep": 9,
    #    "Oct": 10,
    #    "Nov": 11,
    #    "Dec": 12
    # }

    # total = 0
    # minutes = date.today()
    # # curr day
    # total += int(minutes.strftime("%d")) * 1440
    # # curr month - 1
    # total += (months[minutes.strftime("%b")] - 1) * 43800
    # # minutes elapsed since 0000
    # total += int(minutes.strftime("%Y")) * 525600

    # # # 2000-01-01
    # # total += 2000 * 525600
    # # total += 1 * 1440

    # bday = 0
    # bday += int(dob[0:4]) * 525600
    # bday += (int(dob[5:7]) - 1) * 43800
    # bday += int(dob[8:10]) * 1440

    # return total - bday


if __name__ == "__main__":
    main()