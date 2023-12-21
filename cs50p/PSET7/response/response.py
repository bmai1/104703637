import validators


def main():
    print(validate(input("Email: ")))


def validate(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"
    # if email.count('@') != 1 or email.count('.') != 1:
    #     return "Invalid"

    # username, domain = email.split('@')
    # if not username or not domain or not username.isalnum():
    #     return "Invalid"

    # domain, tld = domain.split('.')
    # if not domain.isalpha() or not tld.isalpha():
    #     return "Invalid"

    # return "Valid"


if __name__ == "__main__":
    main()
