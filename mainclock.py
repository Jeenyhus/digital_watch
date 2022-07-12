#python script describing a digital clock

from tkinter import *
from tkinter.ttk import *

from time import strftime

#Title of application

root = Tk()
root.title('Edulution Time')

def time():
    string = strftime('%H:%M:%S:%P')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font =("ds-digital", 80), background = "black", foreground = "green")
label.pack(anchor='center')
time()

mainloop()