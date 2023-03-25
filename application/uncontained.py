from tkinter import *
from application.contained import DateSelector


class Row:
    def __init__(self, master: Frame, row: int, title: str):
        self.label = Label(master, text=f"{title}:")
        self.label.grid(row=row, column=0, sticky="w")

        self.master = master
        self.row = row
        self.title = title


class EntryBox(Row):
    def __init__(self, *args, var: StringVar):
        super(EntryBox, self).__init__(*args)

        self.box = Entry(self.master, textvariable=var, width=40)
        self.box.grid(row=self.row, column=1)

    def bind(self, option: str, function: any):
        self.box.bind(option, function)


class DateRow(Row):
    def __init__(self, *args):
        super(DateRow, self).__init__(*args)

        self.date = DateSelector(self.master)
        self.date.grid(row=self.row, column=1)