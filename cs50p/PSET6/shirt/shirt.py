import os
import sys
from sys import argv
from PIL import Image, ImageOps


def main():
    # check number of command-line arguments
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(argv) == 1:
        sys.exit("No command-line argument")
    # check extensions
    ext = os.path.splitext(argv[1])[-1].lower()
    ext2 = os.path.splitext(argv[2])[-1].lower()
    if (ext != ".jpg" and ext != ".jpeg" and ext != ".png"):
        sys.exit("File is not a jpeg or png")
    if ext != ext2:
        sys.exit("Input and output have different extensions")
    try:
        # open shirt image
        shirt = Image.open("shirt.png")
        # open input image
        before = Image.open(argv[1])
        size = shirt.size
        # resize input
        after = ImageOps.fit(before, size)
        # paste shirt on image and save
        after.paste(shirt, shirt)
        after.save(argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()