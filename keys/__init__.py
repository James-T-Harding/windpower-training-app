from dataclasses import dataclass
import json

KEYFILE = "keys/save.json"

ELEXON = "elexon"
MET = "met"


@dataclass
class Keys:
    met_key: str
    elexon_key: str

    @classmethod
    def from_data(cls, data):
        met_key = data.get(MET, "")
        elexon_key = data.get(ELEXON, "")

        return cls(met_key, elexon_key)


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
