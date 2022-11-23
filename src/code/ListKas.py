import os
from Kas import Kas
import csv
from userLog import *

def convert_array_data_to_real_values(array_data):
    arr_cpy = array_data[:]
    for i in range(4):
        if (i == 0):
            arr_cpy[i] = int(arr_cpy[i])
        if (i == 1):
            arr_cpy[i] = int(arr_cpy[i])
        if (i == 3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def convert_line_to_data(line):
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

def scanKas():
    f = open("src/data/kas.csv", "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    listKas = []
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header) 
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(array_of_data)
        listKas.append(Kas(real_values[0],real_values[1],real_values[2],real_values[3]))
    return listKas

def printArray(listKas) :
    for line in listKas:
        line.printKas()
for files in os.listdir():
    print (files)
    
    