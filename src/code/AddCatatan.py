from userLog import *
from ListKas import *

class AddCatatan():

    def __init__(self, catatanid, deskripsi, tanggal, amount, kategori, tipe, flow):
        self.__catatanid = catatanid
        self.__kasid = getCurrentKas()
        self.__userid = getCurrentUser()
        self.__deskripsi = deskripsi
        self.__tanggal = tanggal
        self.__amount = amount
        self.__kategori = kategori
        self.__tipe = tipe
        self.__flow = flow

    def get_catatan_id(self) -> int:
        return self.__catatanid

    def get_kas_id(self) -> int:
        return self.__kasid
    
    def get_user_id(self) -> int:
        return self.__userid
    
    def get_deskripsi(self) -> str:
        return self.__deskripsi
    
    def get_tanggal(self):
        return self.__tanggal

    def get_amount(self) -> int:
        return self.__amount
    
    def get_kategori(self) -> str:
        return self.__kategori

    def get_tipe(self) -> str:
        return self.__tipe

    def get_flow(self) -> str:
        return self.__flow
    
    #setter
    def set_catatan_id(self, catatanid: int):
        return self.__catatanid == catatanid

    def set_kas_id(self, kasid: int):
        return self.__kasid == kasid
    
    def get_user_id(self, userid: int):
        return self.__userid == userid
    
    def set_deskripsi(self, deskripsi: str):
        return self.__deskripsi == deskripsi
    
    def set_tanggal(self, tanggal):
        return self.__tanggal == tanggal

    def set_amount(self, amount: int):
        return self.__amount == amount
    
    def set_kategori(self, kategori: str):
        return self.__kategori == kategori

    def set_tipe(self, tipe: str):
        return self.__tipe == tipe

    def set_flow(self, flow: str):
        return self.__flow == flow

    def addNewCatatan(self):
        catatan_csv = self.__to_csv()
        catatan_file =  open("./src/data/catatan.csv", "a")
        catatan_file.write(catatan_csv)
        catatan_file.close

    def __to_csv(self) -> str:
        csv_data = [str(self.__dict__[data]) for data in self.__dict__]
        csv = ";".join(csv_data)
        csv += "\n"
        return csv

def updateSaldoKas(idkas: str, amount: int, flow):
    listKas = scanKas()
    with open("./src/data/kas.csv","w",newline="") as f:
        writer = csv.writer(f,delimiter=";")
        list = [["kasid","userid","namakas","saldokas"]]
        for kas in listKas :
            if str(kas.getKasID()) == idkas:
                if flow == "Pemasukan":
                    kas.setSaldoKas(int(kas.getSaldoKas()) + int(amount))
                elif flow == "Pengeluaran":
                    kas.setSaldoKas(int(kas.getSaldoKas()) - int(amount))
            list.append([kas.getKasID(), kas.getUserID(), kas.getNamaKas(), kas.getSaldoKas()])
        writer.writerows(list)
