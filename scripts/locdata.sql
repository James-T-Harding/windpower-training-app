--
-- File generated with SQLiteStudio v3.2.1 on Sat Feb 12 17:33:32 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: date
CREATE TABLE date (date_id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT);

-- Table: locations
CREATE TABLE locations (id INTEGER PRIMARY KEY NOT NULL, latitude REAL, longitude REAL, name TEXT, region TEXT);

-- Table: readings
CREATE TABLE readings (reading_id INTEGER PRIMARY KEY AUTOINCREMENT, reading REAL NOT NULL, time_id INTEGER REFERENCES time (time_id));

-- Table: time
CREATE TABLE time (date_id INTEGER NOT NULL REFERENCES date (date_id), time_id INTEGER PRIMARY KEY AUTOINCREMENT, time TEXT NOT NULL);

-- Table: wind_observations
CREATE TABLE wind_observations (reading_id INTEGER PRIMARY KEY AUTOINCREMENT, gust INTEGER, temperature INTEGER, direction TEXT, speed INTEGER, pressure REAL, time_id REFERENCES time, loc_id INTEGER REFERENCES locations (id));

-- Table: wind_predictions
CREATE TABLE wind_predictions (reading_id INTEGER PRIMARY KEY AUTOINCREMENT, gust INTEGER, temperature INTEGER, direction TEXT, speed INTEGER, pressure REAL, time_id REFERENCES time, loc_id INTEGER REFERENCES locations (id));

-- View: ordered_times
CREATE VIEW ordered_times AS SELECT date AS [date], time AS [time], t.time_id AS time_id
FROM date d 
    JOIN time t ON d.date_id = t.date_id
ORDER BY date, time;

-- View: reading_gaps
CREATE VIEW reading_gaps AS SELECT date, time, t.time_id
FROM date d 
    JOIN time t ON d.date_id = t.date_id
    LEFT JOIN readings r ON t.time_id = r.time_id 
WHERE reading ISNULL;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
