import requests
import json
import sys

try:
    btc_amnt = int(sys.argv[1])
    rspns = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rspns_jsn = rspns.json()
    print(json.dumps(rspns_jsn, indent=2))
    btc_crrnt_prc = float(rspns_jsn["bpi"]["USD"]["rate"].replace(",", ""))
    print(f"USD ${btc_crrnt_prc * btc_amnt:,}")
    
except IndexError:
    print("Missing command-line argument")
    sys.exit()
except ValueError:
    print("Command-line argument is not a number")
except requests.RequestException:
    pass
