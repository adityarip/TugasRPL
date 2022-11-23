from tkinter import *
import tkinter as tk
from userLog import *
import csv

class KasInterface2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        TitleKasInterface = Label(self, text='ppppppp! \n Register Your Self!', width=25, font=('Arial', 48))
        TitleKasInterface.pack()
        

        idCurrentUser = getCurrentUser()

        fileKas = open("./src/data/kas.csv", mode="r", newline="")
        readerKas = csv.reader(fileKas, delimiter=";")

        for row in readerKas:
            print(row)
            if(row[1] == idCurrentUser):
                print(row[2])
                Button(self, text=row[2], width=15, padx=2).pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x720')
        self.resizable(True, True)
        self.title('List Kas')
        for x in range(10):
            self.columnconfigure(x, weight=1)
            self.rowconfigure(x, weight=1)
        self.value = 0

if __name__ == "__main__":
    app = App()
    KasInterface2(app)

    app.mainloop()
        # Frame.__init__(self, parent)
        # Label(self, height=8).pack()
        # TitleLogin = Label(self, text="Welcome to GoArta! \n Please Log In", width=20)
        # TitleLogin.pack()
        # Label(self, height=2).pack()

        # Text1 = Label(self, text="Username")
        # Text1.pack()
        # self.EntryName = Entry(self, width=25)
        # self.EntryName.pack()

        # Text2 = Label(self, text="Password")
        # Text2.pack()
        # self.EntryPass = Entry(self, width=25)
        # self.EntryPass.pack()
        # Label(self, height=1).pack()

        # Button(self, text='Log In', width=15, command=lambda: commandLogin(self, controller))
        # Button1.pack()
        # Label(self, height=3).pack()

        # Label(self, text="Not Having An Account?").pack()
        # Button(self, text='Register', width=15, command=lambda: controller.frames[1].tkraise()).pack()