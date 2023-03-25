from matplotlib.pyplot import *
from pandas import DataFrame
import sqlite3 as sq

db = sq.connect("../NationalWind.db")
c = db.cursor()

query = "SELECT latitude, longitude, speed FROM locations l " \
f"LEFT JOIN ( SELECT * FROM wind_observations v " \
                "JOIN time t ON t.time_id = v.time_id " \
                "WHERE t.time_id = ?) " \
"sel ON sel.loc_id = l.id " \
"WHERE l.region != 'NI' AND l.region IS NOT NULL "

ids = [1, 3, 49, 225]
titles = ["Base", "1 hour", "1 day", "5 days"]


for t_id, ti in zip(ids, titles):
    frame = DataFrame(c.execute(query, [t_id])).dropna()
    lat, long, speed = [frame[n] for n in range(3)]

    speed = [int(s) for s in speed]

    figure(figsize=(4.5, 5.5))
    p1 = scatter(long, lat, c=speed, vmin=0, vmax=25)
    title(ti)

    colorbar(p1)

    savefig(f"../figures/{ti}")