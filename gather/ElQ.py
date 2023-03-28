from requests import get

from keys import load_keys


def get_power(date: str):
    keys = load_keys()
    url = "https://api.bmreports.com/BMRS/B1620/v1"
    params = dict(
        APIKey=keys.elexon_key,
        ServiceType="csv",
        SettlementDate=date,
        Period="*",
    )

    response = get(url, params)
    response.raise_for_status()

    lines = response.text.split('\n')[5:-1]
    data = [line.split(',') for line in lines]

    return [[d[8], float(d[4])] for d in data if d[9] == '"Wind Onshore"']
