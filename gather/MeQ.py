import urllib.request as req

from requests import get

from keys import load_keys
from utility.dtypes import MetData
import json

OBS = "wxobs"
FCS = "wxfcs"

HOUR = "hourly"
HOUR3 = "3hourly"
DAY = "daily"


def query(forecast_type, resolution):
    url = f"http://datapoint.metoffice.gov.uk/public/data/val/{forecast_type}/all/json/all"
    keys = load_keys()
    params = dict(
        key=keys.met_key,
        res=resolution,
    )

    response = get(url, params)
    response.raise_for_status()

    return MetData(response.json())
