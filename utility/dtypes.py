from datetime import datetime, timedelta


class RowInfo:
    def __init__(self, date: datetime, loc_id: int, row: dict[str]):
        self.time = date + timedelta(minutes=int(row['$']))
        self.loc_id = loc_id

        self.row = row

    def gen_params(self, timestamp: int):
        ret = [self.row[p] if p in self.row else None for p in ['G', 'T', 'D', 'S', 'P']]
        ret.extend([timestamp, self.loc_id])

        return ret


class MetData:
    def __init__(self, data: dict):
        dv = data["SiteRep"]["DV"]

        self.type = dv["type"]
        self.readings = dv["Location"]
        self.dataDate = datetime.strptime(dv["dataDate"], "%Y-%m-%dT%H:%M:%SZ")