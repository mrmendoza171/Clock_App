from configuration import *

from tkinter import *
from tkinter import ttk




class Dashboard(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(bg=TERTIARY)



        self.left_column = Frame(self, width=100, bg=SECONDARY)
        self.left_column.grid(row=1, column=0)


        self.center_column = Frame(self, width=100, bg=SECONDARY)
        self.center_column.grid(row=1, column=1)



