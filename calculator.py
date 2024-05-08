from tkinter import *
parent=Tk()
parent.title("Calculator")
parent.iconbitmap('')
a= Entry(parent,width=30,borderwidth=5)
a.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def bclick(num):
    current=a.get()
    a.delete(0,END)
    a.insert(0,str(current)+str(num))

def bclear():
    a.delete(0,END)

def add():
    first_num=a.get()
    global c
    global d
    d="Addition"
    c=int(first_num)
    a.delete(0,END)

def sub():
    first_num=a.get()
    global c
    global d
    d="Subtraction"
    c=int(first_num)
    a.delete(0,END)

def mul():
    first_num=a.get()
    global c
    global d
    d="product"
    c=int(first_num)
    a.delete(0,END)

def div():
    first_num=a.get()
    global c
    global d
    d="Division"
    c=int(first_num)
    a.delete(0,END)

def bequal():
    second_num=a.get()
    a.delete(0,END)

    if d=="Addition":
        a.insert(0, c + int(second_num))

    if d=="Subtraction":
        a.insert(0, c - int(second_num))

    if d=="product":
        a.insert(0, c * int(second_num))

    if d=="Division":
        a.insert(0, c / int(second_num))

button_ac=Button(parent,text="AC",padx=35,pady=15,command=bclear).grid(row=1,column=0)
button_add=Button(parent,text="+",padx=39,pady=15,command=add).grid(row=1,column=2)
button_sub=Button(parent,text="-",padx=39,pady=15,command=sub).grid(row=1,column=3)
button_7=Button(parent,text="7",padx=40,pady=15,command=lambda: bclick(7)).grid(row=2,column=0)
button_8=Button(parent,text="8",padx=40,pady=15,command=lambda: bclick(8)).grid(row=2,column=1)
button_9=Button(parent,text="9",padx=40,pady=15,command=lambda: bclick(9)).grid(row=2,column=2)
button_mul=Button(parent,text="*",padx=39,pady=15,command=mul).grid(row=2,column=3)
button_4=Button(parent,text="4",padx=40,pady=15,command=lambda: bclick(4)).grid(row=3,column=0)
button_5=Button(parent,text="5",padx=40,pady=15,command=lambda: bclick(5)).grid(row=3,column=1)
button_6=Button(parent,text="6",padx=40,pady=15,command=lambda: bclick(6)).grid(row=3,column=2)
button_div=Button(parent,text="/",padx=39,pady=15,command=div).grid(row=3,column=3)
button_1=Button(parent,text="1",padx=40,pady=15,command=lambda: bclick(1)).grid(row=4,column=0)
button_2=Button(parent,text="2",padx=40,pady=15,command=lambda: bclick(2)).grid(row=4,column=1)
button_3=Button(parent,text="3",padx=40,pady=15,command=lambda: bclick(3)).grid(row=4,column=2)
button_0=Button(parent,text="0",padx=40,pady=15,command=lambda: bclick(0)).grid(row=1,column=1)
button_equal=Button(parent,text="=",padx=40,pady=15,command=bequal).grid(row=4,column=3)

parent.mainloop()


