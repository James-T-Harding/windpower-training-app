from requests import get

from gather.errors import MissingAPIKeyError
from keys.file import load_key


def get_power(date: str):
    elexon_key = load_key("elexon_key")

    if not elexon_key:
        raise MissingAPIKeyError

    url = "https://api.bmreports.com/BMRS/B1620/v1"
    params = dict(
        APIKey=elexon_key,
        ServiceType="csv",
        SettlementDate=date,
        Period="*",
    )

    response = get(url, params)
    response.raise_for_status()

    lines = response.text.split('\n')[5:-1]
    data = [line.split(',') for line in lines]

    return [[d[8], float(d[4])] for d in data if d[9] == '"Wind Onshore"']
