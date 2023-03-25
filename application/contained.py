from tkinter import *
from datetime import datetime


class DisplayBox(Listbox):
    def __init__(self, *args, **kwargs):
        super(DisplayBox, self).__init__(*args, **kwargs)

        self.items = []

    def refresh(self, title, items):
        self.configure(width=0)

        self.items = items
        self.delete(0, END)

        self.insert(END, title)

        for item in items:
            self.insert(END, item)


class DateSelector(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.date = IntVar(), IntVar(), IntVar()

        items = \
            Entry(self, width=2, textvariable=self.date[0]), \
            Label(self, text='/'), \
            Entry(self, width=2, textvariable=self.date[1]), \
            Label(self, text='/'), \
            Entry(self, width=4, textvariable=self.date[2])

        for i in range(5):
            items[i].grid(column=i, row=0)

    def get(self):
        day, month, year = [var.get() for var in self.date]

        try:
            dt = datetime(year, month, day)
            return dt

        except ValueError:
            pass


if __name__ == "__main__":
    def p():
        print(sel.get())


    root = Tk()
    sel = DateSelector(root)
    sel.grid(row=0, column=0)

    button = Button(text="GetDate", command=p)
    button.grid(row=1)

    root.mainloop()
