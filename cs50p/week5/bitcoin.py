import sys
import requests


def get_amount(argv):
    amount = 0
    if len(argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(argv) > 2:
        sys.exit("Invalid Usage")
    else:
        try:
            amount = float(argv[1])
        except ValueError:
            sys.exit("Invalid argument, must be a number")
    return amount


def get_bitcoin_rate_float():
    rfloat = 0
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        rfloat = response["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error")
    return rfloat


print(f"${get_bitcoin_rate_float()*get_amount(sys.argv):,.2f}")