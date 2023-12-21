import os
import sys
from sys import argv

# extenstion
ext = os.path.splitext(argv[1])[-1].lower()

# check num command-line args and ext
if len(argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(argv) > 2:
    sys.exit("Too many command-line arguments")
elif ext != ".py":
    sys.exit("Not a python file")

# lines counter
lines_of_code = 0
filename = argv[1]

# count++ if line of code
try:
    file = open(filename, "r")
    for row in file:
        if not row.lstrip().startswith("#") and not row.isspace():
            lines_of_code += 1

# if invalid file
except FileNotFoundError:
    sys.exit("File does not exist")

print(lines_of_code)