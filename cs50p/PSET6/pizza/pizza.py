import os
import sys
from sys import argv
from tabulate import tabulate
import csv


def main():
    # Check for proper command-line usage
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check for .csv extension
    ext = os.path.splitext(argv[1])[-1].lower()
    if ext != ".csv":
        sys.exit("Not a CSV file")
    filename = argv[1]
    create_table(filename)


def create_table(filename):
    # list of dicts
    list = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            # append the dict values in each row
            for element in reader:
                list.append(element)
    # if can't find file
    except FileNotFoundError:
        sys.exit("File does not exist")
    # print table, headers are keys, table format is grid
    print(tabulate(list, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()