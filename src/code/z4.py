from tkinter import *

sn = Tk()

sn.title("GoArta")
sn.geometry("1200x800")

#dasboard
dashboard_text = StringVar()
dashboard_label = Label(sn, text="Dashboard", font=("bold", 18), pady=30, padx=3)
dashboard_label.grid(row=1, column=1)
#dashboard_label.pack()
#kas
kas_text = StringVar()
kas_label = Label(sn, text="Kas", font=("bold",18), pady=30, padx=3)
kas_label.grid(row=2, column=1)
#kas_label.pack()

clicked = StringVar()
clicked.set("Choose Kas")

#dropdown
drop = OptionMenu(sn, clicked, "GoPay", "OVO", "ShoppePay", "BCA", "Mandiri", "BNI", "BRI")
#drop_label = Label(sn, text="Choose Kas", font=("bold", 18))
drop.grid(row=3, column=1, padx=3)
#drop.pack()

#logout
logout_text = StringVar()
logout_label = Label(sn, text="LogOut", font=("bold", 18), pady=430, padx=3)
logout_label.grid(row=10, column=0)



sn.mainloop()



