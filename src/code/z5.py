from tkinter import *

def login():
    login_label = Label(app, text="Please Wait!")
    login_label.pack()

#Create Window Object
app = Tk()

#App Title and Size
app.title("GoArta")
app.geometry("1200x800")

#Welcome
welcome_text = StringVar()
welcome_label = Label(app, text="Welcome to GoArta", font=("bold",18), pady=80)
welcome_label.pack()

#Username
username_text = StringVar()
username_label = Label(app, text="Username", font=("bold",14), pady=20)
username_label.pack()
#username_label.grid(row=0,column=0, sticky=W)
username_entry = Entry(app, textvariable=username_text, width=35)
username_entry.pack()
#username_entry.insert(0, "Enter your username: ")
#username_entry.grid(row=2, column=0, padx=10, pady=10)

#Password
password_text = StringVar()
password_label = Label(app, text="Password", font=("bold",14), pady=20)
password_label.pack()
#password_label.grid(row=2,column=0, sticky=W)
password_entry = Entry(app, textvariable=password_text, width=35)
password_entry.pack()
#password_entry.grid(row=3, column=0)

#LogIn
login_btn = Button(app, text="Log In", font=("bold",14), command=login, padx=50)
#login_btn = Button(app, text="Log In", font=("bold",14), command=login, padx=50, fg="blue", bg="green")
login_btn.pack()

#Account
except_text = StringVar()
except_label  = Label(app, text="Don't Have an Account?", font=("bold",12), pady=20)
except_label.pack()

#SignUp
signup_btn = Button(app, text="Sign Up", font=("bold",14), command=login, padx=50)
#login_btn = Button(app, text="Log In", font=("bold",14), command=login, padx=50, fg="blue", bg="green")
signup_btn.pack()

#Start Program
app.mainloop()
