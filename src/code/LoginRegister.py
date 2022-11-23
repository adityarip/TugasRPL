from tkinter import *
import csv
import tkinter
from User import User
from LoginKlas import LoginKlas
from RegisterKlas import RegisterKlas


def commandLogin(login, controller) -> User:

    newLog = LoginKlas()
    newLog.username = login.EntryName.get()
    newLog.password = login.EntryPass.get()
    if newLog.username == "" or newLog.password == "":
        tkinter.messagebox.showinfo("Error", "Isi username dan password anda")
    else:
        with open("./src/data/user.csv", mode="r", newline="") as fileRead:
            reader = csv.reader(fileRead, delimiter=";")
            found = False
            for row in reader:
                if (row[3] == newLog.username and row[4] == newLog.password):
                    found = True
                    tkinter.messagebox.showinfo("Success", "Log in Berhasil")

                    fileRead = open("./src/data/user_log.csv", mode="r", newline="")
                    reader = csv.reader(fileRead, delimiter=";")
                    newID = 0
                    for baris in reader:
                        newID += 1
                    fileRead.close()

                    fileWrite = open("src/data/user_log.csv", "a",newline='')
                    writer = csv.writer(fileWrite, delimiter=";")
                    writer.writerow([newID, row[0], 0])
                    fileWrite.close()
                                
                    # controller.frames[2] = KasInterface2(controller.container, controller, user)
                    # controller.frames[2].grid(row=0, column=0, sticky=tk.NSEW)
                    controller.change_frame(2)
                    # print("hhhh")
                    # controller.frames[2].tkraise()
                    # print("xxx")
            if(found == False):
                tkinter.messagebox.showinfo("Error", "Username atau password anda salah")
            fileRead.close()

    return

def commandRegister(regis, controller):
    newReg = RegisterKlas()
    newReg.name = regis.Entry1.get()
    newReg.email = regis.Entry2.get()
    newReg.username = regis.Entry3.get()
    newReg.password = regis.Entry4.get()

    if (newReg.name == "" or newReg.email == "" or newReg.username == "" or newReg.password == ""):
        tkinter.messagebox.showinfo("Error", "Isi semua data diri anda")
    else:
        Unique = True
        with open("./src/data/user.csv", mode="r", newline="") as fileRead:
            reader = csv.reader(fileRead, delimiter=";")
            newID = 0
            for row in reader:
                if (row[3] == newReg.username):
                    Unique = False
                newID += 1
            fileRead.close()

        if (Unique == False):
            tkinter.messagebox.showinfo(
                "Error", "Username sudah digunakan. Harap menggunakan username yang lain")
        else:
            with open("./src/data/user.csv", mode="a", newline="") as fileWrite:
                writer = csv.writer(fileWrite, delimiter=";")
                writer.writerow([newID, newReg.name, newReg.email, newReg.username, newReg.password])
                tkinter.messagebox.showinfo("Success", "Register Berhasil")
                fileWrite.close()
            controller.frames[0].tkraise()

class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, height=8).pack()
        TitleLogin = Label(self, text="Welcome to GoArta! \n Please Log In", width=20)
        TitleLogin.pack()
        Label(self, height=2).pack()

        Text1 = Label(self, text="Username")
        Text1.pack()
        self.EntryName = Entry(self, width=25)
        self.EntryName.pack()

        Text2 = Label(self, text="Password")
        Text2.pack()
        self.EntryPass = Entry(self, width=25)
        self.EntryPass.pack()
        Label(self, height=1).pack()

        Button1 = Button(self, text='Log In', width=15, command=lambda: commandLogin(self, controller))
        Button1.pack()
        Label(self, height=3).pack()

        Label(self, text="Not Having An Account?").pack()
        Button(self, text='Register', width=15, command=lambda: controller.frames[1].tkraise()).pack()

class Register(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, height=8).pack()
        TitleLogin = Label(self, text='Welcome to GoArta! \n Register Your Self!', width=25)
        TitleLogin.pack()
        Label(self, height=2).pack()

        Text1 = Label(self, text="Name")
        Text1.pack()
        self.Entry1 = Entry(self, width=25)
        self.Entry1.pack()

        Text2 = Label(self, text="Email")
        Text2.pack()
        self.Entry2 = Entry(self, width=25)
        self.Entry2.pack()

        Text3 = Label(self, text="Username")
        Text3.pack()
        self.Entry3 = Entry(self, width=25)
        self.Entry3.pack()

        Text4 = Label(self, text="Password")
        Text4.pack()
        self.Entry4 = Entry(self, width=25)
        self.Entry4.pack()
        Label(self, height=1).pack()

        Button(self, text='Register', width=15, command=lambda: commandRegister(self, controller)).pack()
        Label(self, height=3).pack()

        Label(self, text="Having An Account?").pack()
        Button(self, text='Log In', width=15, command=lambda: controller.frames[0].tkraise()).pack()