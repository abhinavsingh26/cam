from tkinter import *
from tkinter import messagebox

def Buttontapped():
    messagebox._show("Message", "button clicked" )


root =Tk()

Mylabel = Label(root, text="My First Lebel")
Abutton = Button(root, text="Click me", command = Buttontapped )
Mylabel.pack()
Abutton.pack()

root.mainloop()