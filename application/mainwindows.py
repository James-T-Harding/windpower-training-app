from gather.write import Converter

from application.uncontained import EntryBox
from utility import export
from keys import save_keys, load_keys
from threading import Thread
from tkinter import *


class TrainingScreen(Tk):
    def __init__(self, *args, **kwargs):
        super(TrainingScreen, self).__init__(*args, **kwargs)

        self.title("Training Program (James Harding)")

        self.menu = Menu(self)

        self.saver = export.Saver(self.print, self.clear)
        self.converter = Converter(self.print)

        self.__initialise_menu()

        self.gather_button = Button(text="Update Readings", command=self.thread(self.gather))
        self.gather_button.grid(column=0, row=0, sticky='w')

        self.display = Listbox(width=100, height=25)
        self.display.grid(row=1, column=0, columnspan=2)

    def gather(self):
        self.print("Operation started.")

        self.converter.add_observations()
        self.converter.add_power_readings()

        self.print("Operation finished.")

    def clear(self):
        self.display.delete(0, END)

    def print(self, text):
        self.display.insert(END, text)

    def get_predictions(self):
        self.converter.add_predictions()

        self.print("Operation finished.")

    def key_menu(self):
        KeyAdjustor(self)

    def thread(self, function: any):
        def ret():
            self.clear()

            t = Thread(target=function, daemon=True)
            t.start()

        return ret

    def __initialise_menu(self):
        train, predictions = (self.thread(f) for f in [
            self.saver.train_model,
            self.get_predictions
        ])

        self.menu.add_command(label="Keys", command=self.key_menu)

        modelmenu = Menu(self.menu, tearoff=0)
        modelmenu.add_command(label="Train", command=train)
        modelmenu.add_command(label="Predict", command=predictions)

        self.menu.add_cascade(label="Model", menu=modelmenu)

        exportmenu = Menu(self.menu, tearoff=0)
        exportmenu.add_command(label="Csv", command=self.saver.pre2csv)
        exportmenu.add_command(label="Graph", command=self.saver.pre2graph)

        self.menu.add_cascade(label="Export", menu=exportmenu)

        self.config(menu=self.menu)


class KeyAdjustor(Toplevel):
    def __init__(self, *args, **kwargs):
        super(KeyAdjustor, self).__init__(*args, **kwargs)

        self.title("Key Supplier")

        keys = load_keys()
        self.wind = StringVar(value=keys.met_key)
        self.power = StringVar(value=keys.elexon_key)

        EntryBox(self, 0, "Met Key", var=self.wind)
        EntryBox(self, 1, "Elexon Key", var=self.power)

        button = Button(self, text="Save", command=self.save_keys)
        button.grid(row=2, column=0, sticky="w")

    def save_keys(self):
        save_keys(self.wind.get(), self.power.get())