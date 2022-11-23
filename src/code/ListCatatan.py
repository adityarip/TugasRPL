from Catatan_Keuangan import Catatan_Keuangan
import os


def convert_array_data_to_real_values_catatan(array_data):
    arr_cpy = array_data[:]
    for i in range(4):
        if (i == 0):
            arr_cpy[i] = int(arr_cpy[i])
        if (i == 1):
            arr_cpy[i] = int(arr_cpy[i])
        if (i == 2):
            arr_cpy[i] = int(arr_cpy[i])
        if (i == 5):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def convert_line_to_datas(line):
    split_list = []
    tmp = ''
    for s in line:
        if s == ';':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += s
    if tmp:
        split_list.append(tmp)
    return split_list 


def scanCatatan():
    f = open("src/data/catatan.csv", "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    listCatatan = []
    raw_header = lines.pop(0)
    header = convert_line_to_datas(raw_header) 
    for line in lines:
        array_of_data = convert_line_to_datas(line)
        real_values = convert_array_data_to_real_values_catatan(array_of_data)
        listCatatan.append(Catatan_Keuangan(real_values[0],real_values[1],real_values[2],real_values[3], real_values[4],  real_values[5],  real_values[6],  real_values[7], real_values[8]))
    return listCatatan

'''  
def printArrays(listCatatan) :
    for line in listCatatan:
        line.printCatatan()
for files in os.listdir():
    print (files)
'''

#ini di bawah adalah testing kalau dihapus gapapa
'''
listCatatan = scanCatatan()
printArrays(listCatatan) 

for line in (listCatatan):
    if (line.getFlow() == "pengeluaran"):
        print(line.getAmount())

'''