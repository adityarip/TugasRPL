from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import AddCatatan
from AddCatatan import updateSaldoKas
import ListCatatan
from userLog import *


class AddCatatanInterface(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(width=1280, height=720)

        self.__header_frame = Frame(self, background='lightgrey', width=1536, height=75)
        self.__addCatatan_label = Label(self.__header_frame, text="Tambahkan Catatan Baru", background='lightgrey', font=('Arial', 20))

        self.__header_frame.place(x=0, y=0)
        self.__addCatatan_label.place(x=75, y=10)

        self.__entry_frame = Frame(self)
        self.__entry_frame.place(x=75, y=75)

        self.__entry_frame.columnconfigure(0, weight=1)
        self.__entry_frame.columnconfigure(1, weight=3)

        self.__label_deskripsicatatan = Label(self.__entry_frame, text="Deskripsi Catatan: ",font=('Arial', 14))
        self.__label_deskripsicatatan.grid(column=0, row=0, sticky=W, pady=12)

        self.__label_tanggalcatatan = Label(self.__entry_frame, text="Tanggal: ",font=('Arial', 14))
        self.__label_tanggalcatatan.grid(column=0, row=1, sticky=W, pady=12)

        self.__label_amountcatatan = Label(self.__entry_frame, text="Amount: ",font=('Arial', 14))
        self.__label_amountcatatan.grid(column=0, row=2, sticky=W, pady=12)

        self.__label_kategoricatatan = Label(self.__entry_frame, text="Kategori: ",font=('Arial', 14))
        self.__label_kategoricatatan.grid(column=0, row=3, sticky=W, pady=12)

        self.__label_tipecatatan = Label(self.__entry_frame, text="Tipe: ",font=('Arial', 14))
        self.__label_tipecatatan.grid(column=0, row=4, sticky=W, pady=12)

        self.__label_flowcatatan = Label(self.__entry_frame, text="Flow: ",font=('Arial', 14))
        self.__label_flowcatatan.grid(column=0, row=5, sticky=W, pady=12)

        self.__entry_deskripsicatatan = Entry(self.__entry_frame, width=80, font=('Arial', 12))
        self.__entry_deskripsicatatan.grid(column=1, row=0, padx=10)

        self.__entry_tanggalcatatan = Entry(self.__entry_frame, width=80, font=('Arial', 12))
        self.__entry_tanggalcatatan.grid(column=1, row=1, padx=10)

        self.__entry_amountcatatan = Entry(self.__entry_frame, width=80, font=('Arial', 12))
        self.__entry_amountcatatan.grid(column=1, row=2, padx=10)

        self.__choice_kategoricatatan = ""
        def get_kategori_choice(_=None):
            self.__choice_kategoricatatan = clickedKategori.get()

        clickedKategori = StringVar()
        clickedKategori.set("Choose Kategori")
        self.__drop_kategoricatatan = OptionMenu(self.__entry_frame, clickedKategori, "Makan-Minum", "Transportasi", "Hiburan", "Tabungan", "Lainnya", command=get_kategori_choice)
        self.__drop_kategoricatatan.grid(column=1, row=3, padx=10)

        self.__choice_tipecatatan = ""
        def get_tipe_choice(_=None):
            self.__choice_tipecatatan = clickedTipe.get()

        clickedTipe = StringVar()
        clickedTipe.set("Choose Tipe")
        self.__drop_tipecatatan = OptionMenu(self.__entry_frame, clickedTipe, "Variable", "Fixed", command=get_tipe_choice)
        self.__drop_tipecatatan.grid(column=1, row=4, padx=10)

        self.__choice_flowcatatan = ""
        def get_flow_choice(_=None):
            self.__choice_flowcatatan = clickedFlow.get()

        clickedFlow = StringVar()
        clickedFlow.set("Choose Flow")
        self.__drop_flowcatatan = OptionMenu(self.__entry_frame, clickedFlow, "Pemasukan", "Pengeluaran", command=get_flow_choice)
        self.__drop_flowcatatan.grid(column=1, row=5, padx=10)

        self.button_kembali = Button(self, text="Kembali", background='grey', foreground='white', font=('Arial', 16), command=lambda: self.commandKembali(controller))
        self.button_kembali.grid(column=1, row=1, sticky=W, pady = 10)
        self.button_kembali.place(x=75, y=500)
        
        self.button_addCatatan = Button(self, text="Tambahkan", background='grey', foreground='white',font=('Arial', 16), command=lambda: self.__add_catatan(controller))
        self.button_addCatatan.grid(column=2, row=1, sticky=W, pady = 10)
        self.button_addCatatan.place(x=205, y=500)

    def commandKembali(self, controller):
        controller.change_frame(4)
        return

    def __add_catatan(self, controller):
        catatan_list = ListCatatan.scanCatatan()
        self.__new_catatan = AddCatatan.AddCatatan(len(catatan_list) + 1, self.__entry_deskripsicatatan.get(), self.__entry_tanggalcatatan.get(), self.__entry_amountcatatan.get(), self.__choice_kategoricatatan, self.__choice_tipecatatan,  self.__choice_flowcatatan)
        if self.__new_catatan.get_deskripsi() == "" or self.__new_catatan.get_tanggal() == "" or self.__new_catatan.get_amount() == "" or self.__new_catatan.get_kategori() == "" or self.__new_catatan.get_tipe() == "" or self.__new_catatan.get_flow() == "":
            messagebox.showerror("Error", "Isi Semua Data!")
        else:
            self.__new_catatan.addNewCatatan()
            updateSaldoKas(self.__new_catatan.get_kas_id(), self.__new_catatan.get_amount(), self.__new_catatan.get_flow())
            messagebox.showinfo("Sukses", "Kas Berhasil Ditambahkan")
            controller.change_frame(2)
            return

if __name__ == "__main__":
    window = Tk()
    window.geometry("1280x720")
    new_catatan = AddCatatanInterface(window)
    new_catatan.pack()
    window.mainloop()