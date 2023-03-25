from datetime import datetime, date, time, timedelta
from sqlite3 import connect, PARSE_DECLTYPES
from functools import cached_property

from .constants import DATABASE_NAME
from .sql import REPLACE_WIND_READING, INSERT_OR_IGNORE_WIND_READING, INSERT_OR_IGNORE_TIMESTAMP

from utility.dtypes import MetData


class Interact:
    def __init__(self):
        self._db = connect(DATABASE_NAME, detect_types=PARSE_DECLTYPES)
        self._cursor = self._db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end(commit=exc_type is None)

    def end(self, commit=True):
        if commit:
            self._db.commit()
        self._db.close()

    def insert_timestamps(self, start: datetime, end: datetime, increment: timedelta):
        while start <= end:
            self._cursor.execute(INSERT_OR_IGNORE_TIMESTAMP, [start])
            start += increment

    @cached_property
    def timestamps(self):
        return dict(self._cursor.execute("SELECT timestamp, id FROM timestamps"))


class WindAdder(Interact):
    def __init__(self, predictions: bool = False, replace=False):
        super().__init__()
        self.predictions = predictions
        self.replace = replace

    def add_data(self, data: MetData) -> None:
        for location in data.readings:
            self.add_location_data(location)

    def add_location_data(self, location: dict) -> None:
        location_id = int(location["i"])

        if location_id not in self.location_ids:
            return

        for day in location["Period"]:
            if rep := isinstance(day, dict) and day.get("Rep"):
                d = datetime.strptime(day["value"], "%Y-%m-%dZ")

                for row in rep:
                    if t := isinstance(row, dict) and row.get("$"):
                        dt = d + timedelta(minutes=int(t))

                        data = [row.get(p) for p in ('G', 'T', 'D', 'S', 'P')]
                        data += [self.predictions, self.timestamps[dt], location_id]

                        self._cursor.execute(self.add_method, data)

            else:
                print(f"Data unavailable for {location_id}")

    @property
    def add_method(self):
        return REPLACE_WIND_READING if self.replace else INSERT_OR_IGNORE_WIND_READING

    @cached_property
    def location_ids(self):
        return {row[0] for row in self._cursor.execute("SELECT id FROM locations")}


class PowerAdder(Interact):
    def add_day(self, day: date, plist: list):
        for ps, reading in plist:
            period = int(ps) - 1
            hours = int(period / 2)
            seconds = (period % 2) * 30

            t = time(hours, seconds)
            dt = datetime.combine(day, t)

            self._cursor.execute(
                "UPDATE timestamps SET power_reading = ? WHERE timestamp = ?",
                [reading, dt]
            )

    @cached_property
    def reading_gap_dates(self) -> set[date]:
        return {timestamp.date() for timestamp, in self._cursor.execute("SELECT timestamp FROM power_reading_gaps")}
