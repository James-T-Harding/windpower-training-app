from gather.ElQ import get_power as get_power_readings
from gather.MeQ import HOUR, HOUR3, OBS, FCS, query as get_met_data
from database.builders import WindAdder, PowerAdder
from utility.dtypes import MetData

from datetime import datetime, timedelta, time
from pprint import pprint


def create_log(data: MetData):
    with open("gather/logfile.txt", 'w') as f:
        f.write(f"DataDate: {data.dataDate}\n\n")

        f.write("\nSample of acquired data:\n\n")
        pprint(data.readings[0], f)

        print("Operation finished. Test output written to logfile.txt")


class Converter:
    def __init__(self, printf: any = print):
        self.print = printf

    def add_observations(self):
        data = get_met_data(OBS, HOUR)
        base = data.dataDate - timedelta(days=1, hours=1)
        inc = timedelta(minutes=30)

        with WindAdder() as cursor:
            cursor.insert_timestamps(base + inc, data.dataDate, inc)
            cursor.add_data(data)

        create_log(data)

    def add_predictions(self):
        data = get_met_data(FCS, HOUR3)

        start = datetime.combine(data.dataDate.date(), time())
        end = start + timedelta(days=4, hours=21)

        with WindAdder(predictions=True, replace=True) as cursor:
            cursor.insert_timestamps(start, end, timedelta(hours=3))
            cursor.add_data(data)

    def add_power_readings(self):
        with PowerAdder() as adder:
            for date in adder.reading_gap_dates:
                power_data = get_power_readings(date.strftime("%Y-%m-%d"))
                adder.add_day(date, power_data)
