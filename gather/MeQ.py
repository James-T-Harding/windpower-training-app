from requests import get

from gather.errors import MissingAPIKeyError
from keys.file import load_key
from utility.dtypes import MetData

OBS = "wxobs"
FCS = "wxfcs"

HOUR = "hourly"
HOUR3 = "3hourly"
DAY = "daily"


def query(forecast_type: str, resolution: str) -> MetData:
    url = f"http://datapoint.metoffice.gov.uk/public/data/val/{forecast_type}/all/json/all"
    met_key = load_key("met_key")

    if not met_key:
        raise MissingAPIKeyError

    params = dict(
        key=met_key,
        res=resolution,
    )

    response = get(url, params)
    response.raise_for_status()

    return MetData(response.json())
