import urllib.request as req
from utility.dtypes import MetData
import json

OBS = "wxobs"
FCS = "wxfcs"

HOUR = "hourly"
HOUR3 = "3hourly"
DAY = "daily"

__KEYFILE = "keys/met.json"


def get_key():
    with open(__KEYFILE) as f:
        return json.load(f)


def set_key(key):
    with open(__KEYFILE, 'w') as f:
        json.dump(key, f)


def send(query_text):
    text = req.urlopen(query_text).read().decode()

    return json.loads(text)


def query(forecast_type, resolution):
    readings = send(
        f"http://datapoint.metoffice.gov.uk/public/data/val/{forecast_type}/all/json/all?"
        f"key={get_key()}&res={resolution}"
    )

    return MetData(readings)
