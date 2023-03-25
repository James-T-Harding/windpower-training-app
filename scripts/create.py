from sqlite3 import *


def run(path):
    db = connect(path)
    c = db.cursor()

    with open("create_db.sql") as f:
        text = f.read()

    c.executescript(text)
    db.close()


if __name__ == "__main__":
    run("../NationalWind.db")
