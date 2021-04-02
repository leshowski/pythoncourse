from tkinter import *

window = Tk()

def conversion():
    pesosChilenos = (float(dollars.get())*875)
    t1.delete("1.0",END)
    t1.insert(END,pesosChilenos)

    canadian = (float(dollars.get())*1.3)
    t2.delete("1.0",END)
    t2.insert(END,canadian)

    euros = (float(dollars.get())*0.84)
    t3.delete("1.0",END)
    t3.insert(END,euros)
    
b1 = Button(window,text="Convertir",command=conversion)
b1.grid(row=0,column=0)
#b1.pack()

dollars = StringVar()
e1= Entry(window,textvariable=dollars)
e1.grid(row=0,column=1)

t1 = Text(window,width=10,height=2)
t1.grid(row=1,column=0)

t2 = Text(window,width=10,height=2)
t2.grid(row=1,column=1)

t3 = Text(window,width=10,height=2)
t3.grid(row=1,column=2)

window.mainloop()