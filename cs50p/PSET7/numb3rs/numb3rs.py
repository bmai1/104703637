import re


# regex to find ip adress
def main():
    print(validate(input("IPv4 address: ")))


def validate(ip):
    if re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip):
        return True
    return False


if __name__ == "__main__":
    main()