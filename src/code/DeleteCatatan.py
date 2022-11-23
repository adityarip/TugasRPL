import os
from userLog import *
from ListCatatan import *
import csv

def deleteCatatan():
    # temp_list = scanCatatan()
    # cur_user_id = getCurrentUser()
    # cur_kas_id = getCurrentKas()

    # print(cur_kas_id)
    # print(cur_user_id)
    # print(temp_list)

    #1. This code snippet asks the user for a username and deletes the user's record from file.
    #catatanid;kasid;userid;deskripsi;tanggal;amount;kategori;tipe;flow
    updatedlist=[]
    with open("src/data/catatan.csv",newline="") as f:
      reader=csv.reader(f, delimiter=";") 
      print(getCurrentKas())
      print(getCurrentUser())
      for row in reader: #for every row in the file
            if ((row[1] != getCurrentKas()) or (row[2] != getCurrentUser())): 
                updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      print(updatedlist)
      updatefile(updatedlist)

def updatefile(updatedlist):
    with open("src/data/catatan.csv", "w",newline="") as f:
        Writer=csv.writer(f, delimiter=";")
        Writer.writerows(updatedlist)
        print("File has been updated")

deleteCatatan()