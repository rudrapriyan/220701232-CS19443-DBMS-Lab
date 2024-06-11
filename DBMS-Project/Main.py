
#Main.py
from tkinter import *
from tkinter.font import Font
import os
from tkinter import messagebox
Main_Interface = Tk()
import sqlite3


# Creating Mysql connection
dbconn = sqlite3.connect("./Database/RSgroceries.db")

# Create a cursor to give commands
cursor = dbconn.cursor()


def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=Main_Interface)
    if sure == True:
        Main_Interface.destroy()

Main_Interface.protocol("WM_DELETE_WINDOW", Exit)


def admpg():
    Main_Interface.withdraw()
    os.system("Admin_login.py")
    Main_Interface.deiconify()

def emp():
    Main_Interface.withdraw()
    os.system("Employee.py")
    Main_Interface.deiconify()


# Fixing GUI Dimensions
Main_Interface.geometry("1150x650")
Main_Interface.resizable(0, 0)

# Fixing Title
Main_Interface.title("RS Groceries")

# Fixing GUI Background
Background = PhotoImage(file="./images/Bg_main.png")
Bg_label = Label(Main_Interface, image=Background)
Bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#Fixing GUI Icon
Main_Interface.iconbitmap("./images/Logo.ico")


# Creating Button
font_1 = Font(family="Franklin Gothic Medium",size=15,weight="bold")
# Button 1
button1 = Button(Main_Interface,text="EMPLOYEE",bg="#38b7fe",fg="black",padx=30,pady=10,width=20,font=font_1,activebackground="#38b7fe",activeforeground="black",command=emp)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(borderwidth="0")
button1.place(relx=0.32, rely=0.42, width=180, height=90,anchor=E)

# Button 2
button2 = Button(Main_Interface, text="ADMIN",bg="#38b7fe", fg="black",padx=30,pady=10,width=20,font=font_1,activebackground="#38b7fe",activeforeground="black",command=admpg)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(borderwidth="0")
button2.place(relx=0.70, rely=0.42, width=240, height=90, anchor=W)

dbconn.close()
Main_Interface.mainloop()
