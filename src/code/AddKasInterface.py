from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import AddKas
import ListKas
from userLog import *

class AddKasInterface(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(width=1280, height=720)

        self.__header_frame = Frame(self, background='lightgrey', width=1536, height=75)
        self.__addKas_label = Label(self.__header_frame, text="Tambahkan Kas Baru", background='lightgrey', font=('Arial', 20))

        self.__header_frame.place(x=0, y=0)
        self.__addKas_label.place(x=75, y=10)

        self.__entry_frame = Frame(self)
        self.__entry_frame.place(x=75, y=75)

        self.__entry_frame.columnconfigure(0, weight=1)
        self.__entry_frame.columnconfigure(1, weight=3)

        self.__label_namakas = Label(self.__entry_frame, text="Nama Kas: ",font=('Arial', 14))
        self.__label_namakas.grid(column=0, row=0, sticky=W, pady=12)

        self.__entry_namakas = Entry(self.__entry_frame, width=80, font=('Arial', 12))
        self.__entry_namakas.grid(column=1, row=0, padx=10)

        self.button_kembali = Button(self, text="Kembali", background='grey', foreground='white',font=('Arial', 16), command=lambda: self.commandKembali(controller))
        self.button_kembali.grid(column=1, row=1, sticky=W, pady = 10)
        self.button_kembali.place(x=75, y=500)
        
        self.button_addKas = Button(self, text="Tambahkan", background='grey', foreground='white',font=('Arial', 16), command=lambda: self.__add_kas())
        self.button_addKas.grid(column=2, row=1, sticky=W, pady = 10)
        self.button_addKas.place(x=205, y=500)

    def commandKembali(self, controller):
        controller.change_frame(2)
        return

    def __add_kas(self):
        kas_list = ListKas.scanKas()
        self.__new_kas = AddKas.AddKas(len(kas_list) + 1, self.__entry_namakas.get())
        kas_names = [kas.namakas for kas in kas_list]
        if self.__new_kas.get_nama_kas() in kas_names:
            messagebox.showerror("Error", "Nama Kas sudah Ada!")
        elif self.__new_kas.get_nama_kas() == "":
            messagebox.showerror("Error", "Masukkan Nama Kas")
        else:
            self.__new_kas.addNewKas()
            messagebox.showinfo("Sukses", "Kas Berhasil Ditambahkan")

if __name__ == "__main__":
    window = Tk()
    window.geometry("1280x720")
    new_book = AddKasInterface(window)
    new_book.pack()
    window.mainloop()


