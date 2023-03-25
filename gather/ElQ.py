import urllib.request as req
import json

from keys import load_keys

KEYFILE = "keys/elexon.json"


def get_power(date: str):
    keys = load_keys()

    querystring = f"https://api.bmreports.com/BMRS/B1620/v1?APIKey={keys.elexon_key}&ServiceType=csv&SettlementDate=" \
                  f"{date}&Period=* "

    file = req.urlopen(querystring).read().decode()

    lines = file.split('\n')[5:-1]
    data = [line.split(',') for line in lines]

    p_data = [[d[8], float(d[4])] for d in data if d[9] == '"Wind Onshore"']

    return p_data


def get_key():
    with open(KEYFILE) as f:
        return json.load(f)


def set_key(key):
    with open(KEYFILE, 'w') as f:
        json.dump(key, f)