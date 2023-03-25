--
-- File generated with SQLiteStudio v3.2.1 on Sat Mar 25 18:55:00 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: locations
CREATE TABLE locations (id INTEGER PRIMARY KEY NOT NULL, latitude REAL, longitude REAL, name TEXT, region TEXT);

INSERT INTO locations (id, latitude, longitude, name, region) VALUES (996, 56.69936, -4.19345, 'Loch Rannoch', NULL);
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3002, 60.749, -0.854, 'Baltasound', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3005, 60.139, -1.183, 'Lerwick (S. Screen)', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3008, 59.527, -1.628, 'Fair Isle', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3010, 59.083, -4.404, 'Sule Skerry', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3014, 60.111, -2.063, 'Foula', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3017, 58.954, -2.9, 'Kirkwall', 'os');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3023, 57.358, -7.397, 'South Uist Range', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3026, 58.214, -6.325, 'Stornoway', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3031, 57.725, -4.896, 'Loch Glascarnoch', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3034, 57.859, -5.636, 'Aultbea', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3037, 57.257, -5.809, 'Skye/Lusa', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3039, 57.4175, -5.689, 'Bealach Na Ba', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3041, 56.822, -4.97, 'Aonach Mor Summit', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3044, 58.288, -4.442, 'Altnaharra Saws', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3047, 56.867, -4.708, 'Tulloch Bridge', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3063, 57.206, -3.827, 'Aviemore', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3065, 57.116, -3.642, 'Cairn Gorm Summit', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3066, 57.6494, -3.5606, 'Kinloss', 'gr');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3068, 57.712, -3.322, 'Lossiemouth', 'gr');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3072, 56.879, -3.42, 'Cairnwell', 'ta');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3075, 58.454, -3.089, 'Wick John O Groats Airport', 'he');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3080, 57.077, -2.836, 'Aboyne', 'gr');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3088, 56.852, -2.264, 'Inverbervie', 'gr');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3091, 57.206, -2.202, 'Aberdeen Airport', 'gr');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3100, 56.497, -6.887, 'Tiree', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3105, 55.681, -6.256, 'Islay Airport', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3111, 55.441, -5.699, 'Campbeltown Airport', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3132, 54.859, -4.936, 'West Freugh', 'dg');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3134, 55.907, -4.533, 'Glasgow/Bishopton', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3136, 55.515, -4.585, 'Prestwick Rnas', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3144, 56.326, -3.729, 'Strathallan', 'ta');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3148, 56.423, -4.32, 'Glen Ogle', 'ta');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3153, 54.803, -4.008, 'Dundrennan', 'dg');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3155, 55.627, -3.735, 'Drumalbin', 'st');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3158, 55.709, -2.383, 'Charterhall', 'dg');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3162, 55.311, -3.206, 'Eskdalemuir', 'dg');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3166, 55.928, -3.343, 'Edinburgh/Gogarbank', 'dg');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3171, 56.377, -2.862, 'Leuchars', 'ta');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3204, 54.0849, -4.6321, 'Ronaldsway', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3210, 54.5181, -3.615, 'St. Bees Head', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3212, 54.614, -3.157, 'Keswick', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3214, 54.125, -3.257, 'Walney Island', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3220, 54.933, -2.963, 'Carlisle', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3224, 55.05, -2.553, 'Spadeadam', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3225, 54.501, -2.684, 'Shap', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3226, 54.572, -2.413, 'Warcop', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3227, 54.684, -2.45, 'Great Dun Fell 2', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3230, 55.285, -2.279, 'Redesdale Camp', 'ne');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3238, 55.02, -1.88, 'Albemarle', 'ne');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3240, 55.421, -1.6, 'Boulmer', 'ne');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3257, 54.296, -1.53, 'Leeming', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3261, 54.134, -1.414, 'Dishforth Airfield', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3265, 54.204, -1.39, 'Topcliffe', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3266, 54.045, -1.25, 'Linton On Ouse', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3275, 54.563, -0.863, 'Loftus (Samos)', 'ne');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3281, 54.362, -0.673, 'Fylingdales', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3292, 54.094, -0.174, 'Bridlington Mrsc', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3302, 53.252, -4.537, 'Valley', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3305, 53.093, -3.941, 'Capel Curig', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3313, 53.259, -3.509, 'Rhyl', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3316, 53.497, -3.056, 'Crosby', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3321, 53.174, -2.986, 'Hawarden', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3330, 53.12755, -1.97993, 'Leek', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3344, 53.811, -1.865, 'Bingley Samos', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3351, 53.3598, -2.3805, 'Rostherne No 2', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3354, 53.005, -1.25, 'Watnall', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3373, 53.307, -0.546, 'Scampton', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3377, 53.175, -0.521, 'Waddington', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3379, 53.031, -0.502, 'Cranwell', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3382, 53.867, -0.433, 'Leconfield Sar', 'yh');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3385, 53.473, 0.154, 'Donna Nook', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3391, 53.094, -0.171, 'Coningsby', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3392, 53.088, 0.274, 'Wainfleet', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3405, 52.789, -4.742, 'Aberdaron', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3410, 52.757, -3.464, 'Lake Vyrnwy Saws', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3414, 52.794, -2.663, 'Shawbury', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3462, 52.6111, -0.459, 'Wittering', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3469, 52.873, 0.141, 'Holbeach', 'em');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3482, 52.651, 0.569, 'Marham', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3488, 52.949, 1.127, 'Weybourne', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3502, 52.139, -4.571, 'Aberporth', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3503, 52.344, -3.947, 'Trawsgoed', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3507, 52.063, -3.614, 'Sennybridge', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3520, 52.242, -2.885, 'Shobdon Saws', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3522, 52.083, -2.8, 'Hereford', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3529, 52.148, -2.04, 'Pershore', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3535, 52.48, -1.689, 'Coleshill', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3544, 52.358, -1.33, 'Church Lawford', 'wm');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3560, 52.225, -0.464, 'Bedford', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3590, 52.123, 0.961, 'Wattisham', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3604, 51.708, -5.055, 'Milford Haven C.B.', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3605, 51.713, -4.368, 'Pembrey Sands', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3609, 51.565, -3.981, 'Mumbles Head', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3628, 51.521, -2.576, 'Filton', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3647, 51.86, -1.692, 'Little Rissington (Esaws)', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3649, 51.758, -1.576, 'Brize Norton', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3658, 51.62, -1.097, 'Benson', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3660, 51.68, -0.802, 'High Wycombe', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3672, 51.548, -0.415, 'Northolt', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3680, 51.8067, -0.3602, 'Rothamsted', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3684, 51.896, 0.453, 'Andrewsfield', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3693, 51.554, 0.83, 'Shoeburyness', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3707, 51.089, -4.149, 'Chivenor', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3710, 51.087, -3.608, 'Liscombe', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3716, 51.405, -3.44, 'St-Athan', 'wl');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3740, 51.5031, -1.9924, 'Lyneham', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3743, 51.201, -1.805, 'Larkhill', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3746, 51.161, -1.754, 'Boscombe Down', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3749, 51.149, -1.57, 'Middle Wallop', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3761, 51.238, -0.944, 'Odiham', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3768, 51.279, -0.772, 'Farnborough', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3769, 51.15, -0.2333, 'Charlwood', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3772, 51.479, -0.449, 'Heathrow', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3781, 51.303, -0.09, 'Kenley', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3784, 51.464, 0.314, 'Gravesend-Broadness', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3796, 51.133, 1.348, 'Langdon Bay', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3797, 51.3422, 1.3461, 'Manston', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3803, 49.913, -6.301, 'Scilly St Marys', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3808, 50.218, -5.33, 'Camborne', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3809, 50.085, -5.257, 'Culdrose', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3823, 50.502, -4.667, 'Cardinham', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3827, 50.354, -4.121, 'Mount Batten', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3839, 50.737, -3.405, 'Exeter Airport', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3840, 50.86, -3.239, 'Dunkeswell Aerodrome', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3844, 50.7366, -3.40458, 'Exeter Airport', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3853, 51.006, -2.64, 'Yeovilton', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3857, 50.522, -2.454, 'Isle Of Portland', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3862, 50.779, -1.835, 'Bournemouth Airport', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3866, 50.577, -1.297, 'St Catherines Pt.', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3872, 50.815, -0.923, 'Thorney Island', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3876, 50.836, -0.292, 'Shoreham', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3882, 50.89, 0.319, 'Herstmonceux West End', 'se');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3894, 49.44, -2.6, 'Guernsey', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3895, 49.2079, -2.1955, 'Jersey', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3904, 54.707, -7.577, 'Castlederg', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3907, 55.1604, -6.9492, 'Magilligan', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3911, 54.721, -6.814, 'Lough Fea', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3916, 55.181, -6.153, 'Ballypatrick Forest', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3917, 54.664, -6.224, 'Belfast International Airport', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3923, 54.237, -6.502, 'Glenanne', 'ni');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3952, 51.799, -8.25, 'Roches Point', NULL);
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3953, 51.933, -10.25, 'Valentia Observatory', NULL);
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3976, 54.233, -10.001, 'Belmullet', NULL);
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (3980, 55.366, -7.333, 'Malin Head', NULL);
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (99057, 52.017, -0.6, 'Woburn', 'ee');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (99060, 53.85, -2.467, 'Stonyhurst', 'nw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (99081, 50.767, -3.9, 'North Wyke', 'sw');
INSERT INTO locations (id, latitude, longitude, name, region) VALUES (99142, 54.273, -0.421, 'Scarborough', 'yh');

-- Table: timestamps
CREATE TABLE timestamps (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TIMESTAMP NOT NULL UNIQUE, power_reading REAL);

-- Table: wind_readings
CREATE TABLE wind_readings (id INTEGER PRIMARY KEY AUTOINCREMENT, gust INTEGER, temperature INTEGER, direction TEXT, speed INTEGER, pressure REAL, is_prediction BOOLEAN DEFAULT (0), timestamp_id INTEGER REFERENCES timestamps, loc_id INTEGER REFERENCES locations (id), UNIQUE (is_prediction, timestamp_id, loc_id));

-- View: power_reading_gaps
CREATE VIEW power_reading_gaps AS SELECT timestamp, t.id
FROM timestamps t
    JOIN wind_readings wr ON t.id = wr.timestamp_id AND wr.is_prediction = 0
WHERE t.power_reading ISNULL;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;