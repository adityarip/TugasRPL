from tkinter import *
import numpy as np
import matplotlib.pyplot as plt 
from ListCatatan import *
from userLog import *

# root = Tk()
# root.title("Visualisasi Catatan Keuangan")
# root.geometry("400x200")

def piechart():
    list_catatan = scanCatatan()
    array_pengeluaran = []
    array_label_pengeluaran = []
    array_percentages = []
    tuple_explode = ()
    total_pengeluaran = 0

    for line in (list_catatan):
        if (str(line.getUserID()) == getCurrentUser() and str(line.getKasID()) == getCurrentKas() and line.getFlow() == "pengeluaran"):
            array_pengeluaran.append(line.getAmount())
            array_label_pengeluaran.append(line.getKategori())

    for i in range(0, len(array_pengeluaran)):
        array_pengeluaran[i] = int(array_pengeluaran[i])
        total_pengeluaran += array_pengeluaran[i]

    for i in range (0, len(array_pengeluaran)):
        this_amount = array_pengeluaran[i]
        this_percentage = "{:.2f}".format(this_amount / total_pengeluaran)
        array_percentages.append(this_percentage)
    '''     
    for i in range(0, len(array_percentages)):
        array_percentages[i] = float(array_percentages[i])
        total_pengeluaran += array_percentages[i]
    '''
    print(array_pengeluaran)
    print(array_percentages)
    print(array_label_pengeluaran)

    sourceDict = {}
    for i, j in zip(array_label_pengeluaran, array_pengeluaran):
        if not i in sourceDict:
            sourceDict.update({i: j})
        else:
            sourceDict[i] += j

    for x in range(len(sourceDict)):
        tuple_explode = tuple_explode + (0.1,)
    visualisasi_values = np.array(array_pengeluaran)
    labels_pie = array_label_pengeluaran

    plt.pie(sourceDict.values(), labels = sourceDict.keys(),explode=tuple_explode, autopct='%1.1f%%')
    plt.title("Visualisasi Kas")
    plt.show()


# viz_button = Button(root, text = "Tampilkan Visualisasi", command =piechart)
# viz_button.pack()

# root.mainloop()

