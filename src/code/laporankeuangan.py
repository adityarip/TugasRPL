from tkinter import *
import tkinter as tk
from userLog import *
import csv
from lapvisualisasi import *

def pindahTambahKas(controller):
    controller.change_frame(5)
    return

def kembali(controller):
    controller.change_frame(2)
    return

class CatatanInterface(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        TitleCatatanInterface = Label(self, text='Catatan Keuangan Milikmu:', width=25, font=('Arial', 20))
        TitleCatatanInterface.place(x=0,y=0)

        tombolBack = Button(self, text="Back", width=15, pady=10, command=lambda:kembali(controller)).place(x=50,y=50)
        tombolTambahKas = Button(self, text="Tambah Catatan", width=15, pady=10, command=lambda:pindahTambahKas(controller)).place(x=200,y=50)
        tombolVisualisasi = Button(self, text="Lihat Visualisasi", width=15, pady=10, command=lambda:piechart()).place(x=350,y=50)

        idCurrentKas = getCurrentKas()
        print(idCurrentKas)
        fileCatatan = open("./src/data/catatan.csv", mode="r", newline="")
        readerCatatan = csv.reader(fileCatatan, delimiter=";")
        i = 100
        for row in readerCatatan:
            if(row[1] == idCurrentKas):
                print(row[3])
                i = i+100
                Frame(self, background="lightgrey",width=1536, height=80).place(x=0,y=i-20)
                Label(self, background="lightgrey",text=row[3], width=15, pady= 10).place(x=50,y=i)
                Label(self, background="lightgrey",text=row[4], width=15, pady= 10).place(x=450, y=i)
                Label(self, background="lightgrey",text=row[5], width=15, pady= 10).place(x=550, y=i)
                Label(self, background="lightgrey",text=row[6], width=15, pady= 10).place(x=650, y=i)
                Label(self, background="lightgrey",text=row[8], width=15, pady= 10).place(x=750, y=i)
                Button(self, text="Ubah", width=15, pady=10, background="blue").place(x=950,y=i)
                Button(self, text="Hapus", width=15, pady=10, background="red").place(x=1050,y=i)


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
    CatatanInterface(app)

    app.mainloop()


