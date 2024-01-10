# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from test2 import bin
import string

# Create an instance of tkinter frame
win= Tk()
l = []

ls = []
# Set the size of the tkinter window
win.geometry("700x350")
c = 0

# Define a function to show the popup message
def show_msg():
   global l
   global ls
   ls.append(l)
   l = []
   global c
   c = 0
   ct = str(c)
   label.config(text=ct)

b = bin()
def do():
    global ls
    count = 0
    global c
    c = 0
    ct = str(c)
    label.config(text='do')
    for i in ls:

        s = " ".join(i)
        print(";"+string.ascii_uppercase[count], len(i))
        count += 1
        b.binary(s)

def undo():
    global l
    global c
    c = 0
    l = []
    ct = str(c)
    label.config(text=ct)

def show_msg11():
    l.append("6,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg12():
    l.append("6,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg13():
    l.append("6,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg14():
    l.append("6,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg15():
    l.append("6,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg21():
    l.append("5,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg22():
    l.append("5,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg23():
    l.append("5,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg24():
    l.append("5,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg25():
    l.append("5,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg31():
    l.append("4,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg32():
    l.append("4,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg33():
    l.append("4,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg34():
    l.append("4,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg35():
    l.append("4,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg41():
    l.append("3,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg42():
    l.append("3,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg43():
    l.append("3,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg44():
    l.append("3,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg45():
    l.append("3,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg51():
    l.append("2,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg52():
    l.append("2,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg53():
    l.append("2,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg54():
    l.append("2,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg55():
    l.append("2,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg61():
    l.append("1,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg62():
    l.append("1,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg63():
    l.append("1,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg64():
    l.append("1,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg65():
    l.append("1,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg71():
    l.append("0,0")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg72():
    l.append("0,1")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg73():
    l.append("0,2")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg74():
    l.append("0,3")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


def show_msg75():
    l.append("0,4")
    global c
    c += 1
    ct = str(c)
    label.config(text=ct)


label = Label(win,text= f"{c}", font=("Courier", 100))

label.pack()
ttk.Button(win, text= "o", width=5, command=show_msg11).place(x=50, y=50)
ttk.Button(win, text= "o", width=5, command=show_msg12).place(x=100, y=50)
ttk.Button(win, text= "o", width=5, command=show_msg13).place(x=150, y=50)
ttk.Button(win, text= "o", width=5, command=show_msg14).place(x=200, y=50)
ttk.Button(win, text= "o", width=5, command=show_msg15).place(x=250, y=50)
ttk.Button(win, text= "o", width=5, command=show_msg21).place(x=50, y=100)
ttk.Button(win, text= "o", width=5, command=show_msg22).place(x=100, y=100)
ttk.Button(win, text= "o", width=5, command=show_msg23).place(x=150, y=100)
ttk.Button(win, text= "o", width=5, command=show_msg24).place(x=200, y=100)
ttk.Button(win, text= "o", width=5, command=show_msg25).place(x=250, y=100)
ttk.Button(win, text= "o", width=5, command=show_msg31).place(x=50, y=150)
ttk.Button(win, text= "o", width=5, command=show_msg32).place(x=100, y=150)
ttk.Button(win, text= "o", width=5, command=show_msg33).place(x=150, y=150)
ttk.Button(win, text= "o", width=5, command=show_msg34).place(x=200, y=150)
ttk.Button(win, text= "o", width=5, command=show_msg35).place(x=250, y=150)
ttk.Button(win, text= "o", width=5, command=show_msg41).place(x=50, y=200)
ttk.Button(win, text= "o", width=5, command=show_msg42).place(x=100, y=200)
ttk.Button(win, text= "o", width=5, command=show_msg43).place(x=150, y=200)
ttk.Button(win, text= "o", width=5, command=show_msg44).place(x=200, y=200)
ttk.Button(win, text= "o", width=5, command=show_msg45).place(x=250, y=200)
ttk.Button(win, text= "o", width=5, command=show_msg51).place(x=50, y=250)
ttk.Button(win, text= "o", width=5, command=show_msg52).place(x=100, y=250)
ttk.Button(win, text= "o", width=5, command=show_msg53).place(x=150, y=250)
ttk.Button(win, text= "o", width=5, command=show_msg54).place(x=200, y=250)
ttk.Button(win, text= "o", width=5, command=show_msg55).place(x=250, y=250)
ttk.Button(win, text= "o", width=5, command=show_msg61).place(x=50, y=300)
ttk.Button(win, text= "o", width=5, command=show_msg62).place(x=100, y=300)
ttk.Button(win, text= "o", width=5, command=show_msg63).place(x=150, y=300)
ttk.Button(win, text= "o", width=5, command=show_msg64).place(x=200, y=300)
ttk.Button(win, text= "o", width=5, command=show_msg65).place(x=250, y=300)
ttk.Button(win, text= "o", width=5, command=show_msg71).place(x=50, y=350)
ttk.Button(win, text= "o", width=5, command=show_msg72).place(x=100, y=350)
ttk.Button(win, text= "o", width=5, command=show_msg73).place(x=150, y=350)
ttk.Button(win, text= "o", width=5, command=show_msg74).place(x=200, y=350)
ttk.Button(win, text= "o", width=5, command=show_msg75).place(x=250, y=350)


ttk.Button(win, text= "ok", width=5, command=show_msg).place(x=300, y=400)

ttk.Button(win, text= "Do", width=5, command=do).place(x=100, y=400)

ttk.Button(win, text= "Undo", width=5, command=undo).place(x=0, y=400)

win.mainloop()