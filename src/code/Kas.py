from csv import writer

class Kas:

    def __init__(kas):
        kas.kasid = 0
        kas.userid = "userid"
        kas.namakas = "namakas"
        kas.saldokas = "saldokas"

    def __init__(kas, kasid, userid, namakas, saldokas):
        kas.kasid = kasid
        kas.userid = userid
        kas.namakas = namakas
        kas.saldokas = saldokas

    def printKas(kas):
        print("ID User : " + str(kas.userid))
        print("ID Kas : " + str(kas.kasid))
        print("Nama Kas : " + kas.namakas)
        print("Saldo Kas : " + str(kas.saldokas))

    def getKasID(kas):
        return kas.kasid

    def getUserID(kas):
        return kas.userid

    def getNamaKas(kas):
        return kas.namakas
    
    def getSaldoKas(kas):
        return kas.saldokas

    def setKasID(kas, kasid):
        kas.kasid = kasid

    def setUserID(kas, userid):
        kas.userid = userid

    def setNamaKas(kas, namakas):
        kas.namakas = namakas
    
    def setSaldoKas(kas, saldokas):
        kas.saldokas = saldokas