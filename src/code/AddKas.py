import os
from userLog import *
class AddKas():

    def __init__(self, kasid, namakas):
        self.__kasid = kasid
        self.__userid = getCurrentUser()
        self.__namakas = namakas
        self.__saldokas = 0

    def get_user_id(self) -> int:
        return self.__userid
    
    def get_kas_id(self) -> int:
        return self.__kasid

    def get_nama_kas(self) -> str:
        return self.__namakas

    def get_saldo_kas(self) -> int:
        return self.__saldokas

    def set_user_id(self, userid: int):
        return self.__userid == userid
        
    def set_kas_id(self, kasid: int):
        return self.__kasid == kasid

    def set_nama_kas(self, namakas: str):
        return self.__namakas == namakas

    def set_saldo_kas(self, saldokas: int):
        return self.__saldokas == saldokas

    def addNewKas(self):
        kas_csv = self.__to_csv()
        kas_file =  open("./src/data/kas.csv", "a")
        kas_file.write(kas_csv)
        kas_file.close

    def __to_csv(self) -> str:
        csv_data = [str(self.__dict__[data]) for data in self.__dict__]
        csv = ";".join(csv_data)
        csv += "\n"
        return csv



