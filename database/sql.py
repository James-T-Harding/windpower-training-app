GET_WIND_SPEEDS_FOR_TIME_ID = (
    "SELECT wr.speed FROM locations l "
        "LEFT JOIN ("
            "SELECT * FROM wind_readings v "
                "JOIN time t ON t.time_id = v.time_id AND v.is_prediction=?"
            "WHERE t.time_id = ?"
        ") wr ON wr.loc_id = l.id "
    "WHERE l.region != 'NI' AND l.region IS NOT NULL"
)

INSERT_OR_IGNORE_TIMESTAMP = """
    INSERT OR IGNORE INTO timestamps (timestamp) VALUES (?)
"""

INSERT_OR_IGNORE_WIND_READING = """
    INSERT OR IGNORE INTO wind_readings
    (gust, temperature, direction, speed, pressure, is_prediction, timestamp_id, loc_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

REPLACE_WIND_READING = """
    REPLACE INTO wind_readings
    (gust, temperature, direction, speed, pressure, is_prediction, timestamp_id, loc_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""
