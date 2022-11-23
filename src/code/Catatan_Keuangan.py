class Catatan_Keuangan:
    def __init__(self, catatanid, kasid, userid, deskripsi, tanggal, amount, kategori, tipe, flow):
        self.catatanid = catatanid
        self.kasid = kasid
        self.userid = userid
        self.deskripsi = deskripsi
        self.tanggal = tanggal
        self.amount = amount
        self.kategori = kategori
        self.tipe = tipe
        self.flow = flow

    #getter
    def getCatatanID(self):
        return self.catatanid
    
    def getKasID(self):
        return self.kasid

    def getUserID(self):
        return self.userid

    def getDeskripsi(self):
        return self.deskripsi

    def getTanggal(self):
        return self.tanggal

    def getAmount(self):
        return self.amount

    def getKategori(self):
        return self.kategori

    def getTipe(self):
        return self.tipe

    def getFlow(self):
        return self.flow
        

    #setter

    def setCatatanID(self, catatanid):
        self.catatanid = catatanid
    
    def setKasID(self, kasid):
        self.kasid = kasid

    def setUserID(self, userid):
        self.userid = userid

    def setDeskripsi(self, deskripsi):
        self.deskripsi = deskripsi

    def setTanggal(self, tanggal):
        self.tanggal = tanggal

    def setAmount(self, amount):
        self.amount = amount

    def setKategori(self, kategori):
        self.kategori = kategori

    def setTipe(self, tipe):
        self.tipe = tipe
        
    def setFlow(self, flow):
        self.flow = flow

    def printCatatan(self):
        print("ID Catatan : " + str(self.catatanid))
        print("ID Kas : " + str(self.kasid))
        print("ID User : " + str(self.userid))
        print("Deskripsi : " + str(self.deskripsi))
        print("Tanggal : " + str(self.tanggal))
        print("Amount : " + str(self.amount))
        print("Kategori : " + str(self.kategori))
        print("Tipe : " + str(self.tipe))
        print("Flow : " + str(self.flow))
