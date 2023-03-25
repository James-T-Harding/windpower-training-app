from sqlite3 import connect

from .constants import DATABASE_NAME
from.sql import GET_WIND_SPEEDS_FOR_TIME_ID


def with_connection(func):
    def connected_function(*args, **kwargs):
        with connect(DATABASE_NAME) as conn:
            output = func(conn.cursor(), *args, **kwargs)
        return output

    return connected_function


@with_connection
def get_commons(cursor, *tables):
    query = "SELECT timestamp, id FROM timestamps"

    for table in tables:
        query += f"JOIN {table} ON o.time_id = {table}.time_id "

    return cursor.execute(query).fetchall()


@with_connection
def even(cursor, t_id, predictions=False):
    speeds = [s for s, in cursor.execute(GET_WIND_SPEEDS_FOR_TIME_ID, [predictions, t_id])]

    if any(speeds):
        return speeds


@with_connection
def powers(cursor):
    return dict(cursor.execute("SELECT time_id, reading FROM readings"))