from pyfiglet import Figlet
import sys
import random

# check right number of command line arguments
if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")

# if 2 command line arguments in format "-f font_name"
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "-font":
        sys.exit("Invalid usage")

    # see if font name is valid
    try:
        f = Figlet(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")

    print(f.renderText(input("Text: ")))

# if no command line arguments
else:
    f = Figlet()
    # random.choice from list of fonts
    f = Figlet(font=random.choice(f.getFonts()))
    print(f.renderText(input("Text: ")))






