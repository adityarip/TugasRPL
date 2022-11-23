import tkinter as tk
from tkinter import messagebox

from User import *
from LoginRegister import Login, Register
from KasInterface import KasInterface
from AddKasInterface import AddKasInterface
from laporankeuangan import CatatanInterface
from AddCatatanInterface import AddCatatanInterface

class tkinterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.container = tk.Frame(self)
        self.container.pack(expand=1, fill=tk.BOTH)
        self.geometry('1200x700')
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        self.frames = {}

        user = User("", "", "", "", "")

        self.frames[0] = Login(self.container, self)
        self.frames[0].grid(row=0, column=0, sticky=tk.NSEW)

        self.frames[1] = Register(self.container, self)
        self.frames[1].grid(row=0, column=0, sticky=tk.NSEW)

        # self.frames[2] = KasInterface2(self.container, self)
        # self.frames[2].grid(row=0, column=0, sticky=tk.NSEW)

        self.frames[0].tkraise()

    def change_frame(self, idx):
        if(idx==2):
            # self.frames[2] = KasInterface(self.container, self)
            # self.frames[2].grid(row=0, column=0, sticky=tk.NSEW)
            # self.frames[2].tkraise()
            self.frames[2] = KasInterface(self.container, self)
            self.frames[2].grid(row=0, column=0, sticky=tk.NSEW)
            self.frames[2].tkraise()

        if(idx==3):
            self.frames[3] = AddKasInterface(self.container, self)
            self.frames[3].grid(row=0, column=0, sticky=tk.NSEW)
            self.frames[3].tkraise()
        if(idx==4):
            self.frames[4] = CatatanInterface(self.container, self)
            self.frames[4].grid(row=0, column=0, sticky=tk.NSEW)
            self.frames[4].tkraise()
        if(idx==5):
            self.frames[5] = AddCatatanInterface(self.container, self)
            self.frames[5].grid(row=0, column=0, sticky=tk.NSEW)
            self.frames[5].tkraise()
        return

app = tkinterApp()
app.title("GoArta")

app.mainloop()