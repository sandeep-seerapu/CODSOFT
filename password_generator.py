from tkinter import*
import random
import string
parent=Tk()
parent.title("PASSWORD GENERATOR")
def password_generator():
    try:
        length=int(a.get())
        characters=string.digits+string.ascii_letters+string.punctuation.replace('<','').replace('>','')
        password=''.join(random.choice(characters) for i in range(length))
        Label2.config(text="Generated Password:"+password)
        if length<=0:
            raise ValueError
    except ValueError:
        Label2.config(text="invalid entry")   

Label1=Label(parent,text="Enter length of the password:")
Label1.pack()
a=Entry(parent)
a.pack()
b1=Button(parent,text="Generate Password",command=password_generator)
b1.pack()
Label2=Label(parent,text="")
Label2.pack()
parent.mainloop()

