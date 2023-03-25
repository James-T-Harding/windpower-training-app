from sqlite3 import *
from database.constants import DATABASE_NAME
from os import sep


def run(path):
    db = connect(path)
    c = db.cursor()

    with open("create_db.sql") as f:
        text = f.read()

    c.executescript(text)
    db.close()


if __name__ == "__main__":
    run(sep.join(['..', DATABASE_NAME]))
