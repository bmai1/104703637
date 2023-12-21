import os
import csv
import sys
from sys import argv

def main():
    if len(argv) == 1:
        sys.exit("No command-line argument")
    # check for .csv
    ext = os.path.splitext(argv[1])[-1].lower()
    # check proper usage
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ext != ".csv":
        sys.exit("Not a CSV file")
    before_file = argv[1]
    after_file = argv[2]
    split(before_file, after_file)


def split(before_file, after_file):
    first = []
    last = []
    house = []
    try:
        with open(before_file, "r") as infile:
            reader = csv.DictReader(infile)
            for name in reader:
                house.append(name["house"])
                # creating arrays splitting first and last names
                names = name["name"].split(", ")
                first.append(names[1])
                last.append(names[0])
        with open(after_file, "w") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            # looping through arrays, writing rows into after.csv
            for first, last, house in zip(first, last, house):
                writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read file {filename}")


if __name__ == "__main__":
    main()