import json

from keys.constants import MET, ELEXON
from keys.dataclasses import Keys

KEYFILE = "keys/save.json"


def save_keys(met_key=None, elexon_key=None):
    data = {}

    if met_key:
        data[MET] = met_key

    if elexon_key:
        data[ELEXON] = elexon_key

    with open(KEYFILE, "w") as f:
        json.dump(data, f)


def load_keys():
    try:
        with open(KEYFILE) as f:
            data = json.load(f)

    except FileNotFoundError:
        data = {}

    return Keys.from_data(data)


def load_key(key):
    return getattr(load_keys(), key)
