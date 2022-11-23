from tkinter import *
import tkcalendar
from datetime import timedelta

root = Tk()

def date_range(start,stop):
    global dates # If you want to use this outside of functions
     
    dates = []
    diff = (stop-start).days
    for i in range(diff+1):
        day = start + timedelta(days=i)
        dates.append(day)
    cal = [cal.strftime("%d-%m-%Y") for cal in dates]
    if cal:
        print(cal) # Print it, or even make it global to access it outside this
    else:
        print('Pastikan masukan tanggal sudah benar')

date1 = tkcalendar.DateEntry(root)
date1.pack(padx=10,pady=10)

date2 = tkcalendar.DateEntry(root)
date2.pack(padx=10,pady=10)

Button(root,text='Find range',command=lambda: date_range(date1.get_date(),date2.get_date())).pack() 

root.mainloop()