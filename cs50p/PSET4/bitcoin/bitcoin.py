import requests
import sys
from sys import argv

# check valid usage
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(argv[1])
except ValueError:
    sys.exit("Invalid command-line argument")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin = response.json()
# go through dict to find USD rate and turn it into a float after removing commas
usd_rate = float(bitcoin["bpi"]["USD"]["rate"].replace(",", ""))
# format commas again
print(f"${(usd_rate * n):,.4f}")


