from matplotlib.pyplot import *
from matplotlib.dates import DayLocator, HourLocator
from learning.dbbignetwork import *
from datetime import datetime, timedelta
import tkinter.filedialog as fd
import csv
import joblib


MODEL = "learning/ModelDetails.joblib"


class Saver:
    def __init__(self, printf: any = print, clear: any = print):
        self.print = printf
        self.clear = clear

    def pre2csv(self):
        filetypes = (
            ('Comma Separated Variables', '*.csv'),
        )

        self.clear()

        name = ask_name(filetypes)
        times, predictions = get_predictions()

        if not name.endswith(".csv"):
            name += '.csv'

        try:
            with open(name, 'w', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(["Date", "Time", "Result"])
                writer.writerows([dt.date(), dt.time(), prediction] for dt, prediction in zip(times, predictions))

                self.print("File successfully saved.")

        except OSError as e:
            print(f"Error saving {e}")

    def pre2graph(self):
        filetypes = (
            ('Portable Network Graphics', '*.png'),
        )

        self.clear()

        name = ask_name(filetypes)
        times, predictions = get_predictions()

        fig, ax = subplots()

        fig.autofmt_xdate()

        ax.plot(times, predictions)
        ax.xaxis.set_major_locator(DayLocator())
        ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))

        ax.set_title(f"Predictions for {times[0].date()} to {times[-1].date()}")
        ax.set_ylabel("Power (MW)")
        ax.set_xlabel("Date")

        try:
            savefig(name)
            self.print("File successfully saved.")

        except OSError as e:
            print(f"Error saving {e}")

        close()

    def train_model(self):
        self.print("Acquiring readings...")
        readings = get_readings()

        self.print(f"{len(readings)} readings retrieved. Training model...")
        args = train(readings, [484], "logistic", "adam", 100)

        joblib.dump(args, MODEL)
        self.print("Model trained.")


def get_predictions():
    start = datetime.today()
    end = start + timedelta(days=2)

    times, winds = get_predictions(start, end)

    args = joblib.load(MODEL)

    predictions = predict(winds, *args)

    return times, predictions


def ask_name(filetypes):
    name = fd.asksaveasfilename(filetypes=filetypes)

    return name
