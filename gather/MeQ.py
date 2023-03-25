import urllib.request as req

from keys import load_keys
from utility.dtypes import MetData
import json

OBS = "wxobs"
FCS = "wxfcs"

HOUR = "hourly"
HOUR3 = "3hourly"
DAY = "daily"


def query(forecast_type, resolution):
    keys = load_keys()
    query_text = (
        f"http://datapoint.metoffice.gov.uk/public/data/val/{forecast_type}/all/json/all?"
        f"key={keys.met_key}&res={resolution}"
    )

    response = req.urlopen(query_text).read().decode()
    data = json.loads(response)

    return MetData(data)
