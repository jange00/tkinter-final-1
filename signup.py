from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import os
sys.path.insert(1,"C:\\Users\\DELL\\Desktop\\TkProject\\1")
# import tkinter as tk


window =Tk()
window.title("BikeBreeze")
window.geometry("1000x500")
window.resizable(False,False)

img0= PhotoImage(file="signup.png")
label1=Label(window, image= img0)
label1.pack(fill=X)


frame=Frame(window,width=600,height=330,bg='white')
frame.place(x=0,y=70)

label=Label(frame,text="Registration",fg="Orange",bg="white",font=('Gabriola','25','bold'))
label.place(x=160,y=0)

def openlogin():
   window.destroy()
   import login



def enter(event):
    firstname.delete(0,'end')
    
def leave(event):
    a=firstname.get()
    if a=='':
      firstname.insert(0,'First Name')
firstname=Entry(frame,text="First Name",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
firstname.place(x=60,y=60)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=20,y=80)  
     
firstname.insert(1,'First Name')
firstname.bind('<FocusIn>',enter)
firstname.bind('<FocusOut>',leave)

def enter(event):
    lastname.delete(0,'end')
    
def leave(event):
    a=lastname.get()
    if a=='':
      lastname.insert(0,'Last Name')
lastname=Entry(frame,text="Last Name",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
lastname.place(x=285,y=60)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=230,y=80)  
     
lastname.insert(1,'Last Name')
lastname.bind('<FocusIn>',enter)
lastname.bind('<FocusOut>',leave)



def enter(event):
    phone_number.delete(0,'end')
    
def leave(event):
    a=phone_number.get()
    if a=='':
        phone_number.insert(0,'Phone Number')
    
phone_number=Entry(frame,text="Phone Numbe",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
phone_number.place(x=130,y=105)

y=Frame(frame,width=250,height=2,bg='black')
y.place(x=80,y=125) 

phone_number.insert(1,'Phone Numbe')
phone_number.bind('<FocusIn>',enter)
phone_number.bind('<FocusOut>',leave)

def enter(event):
    email.delete(0,'end')
    
def leave(event):
    a=email.get()
    if a=='':
        email.insert(0,'Email')
        
email=Entry(frame,text="Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
email.place(x=130,y=150)

x=Frame(frame,width=250,height=2,bg='black')
x.place(x=80,y=170)

email.insert(1,'Email')
email.bind('<FocusIn>',enter)
email.bind('<FocusOut>',leave)

def enter(event):
    password.delete(0,'end')
    
def leave(event):
    a=password.get()
    if a=='':
        password.insert(0,'Password')
        
password=Entry(frame,text="Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show='*')
password.place(x=140,y=195)

w=Frame(frame,width=250,height=2,bg='black')
w.place(x=80,y=215)

password.insert(1,'Password')
password.bind('<FocusIn>',enter)
password.bind('<FocusOut>',leave)

# def hide1():
#     print('Hide')
#     openeye.config(file='eye1.png')
#     password.config(show='*')
#     eyebutton.config(command=show1)
    
# def show1():
#     openeye.config(file='eye.png')
#     password.config(show='')
#     eyebutton.config(command=hide1)

# openeye= PhotoImage(file='eye1.png')
# eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show1)
# eyebutton.place(x=310,y=188)
    


def enter(event):
    confirm_password.delete(0,'end')
    
def leave(event):
    a=confirm_password.get()
    if a=='':
        confirm_password.insert(0,'Confirm Password')
        
confirm_password=Entry(frame,text="Confirm Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show='*')
confirm_password.place(x=140,y=240)

v=Frame(frame,width=250,height=2,bg='black')
v.place(x=80,y=260)

confirm_password.insert(1,'Confirm Password')
confirm_password.bind('<FocusIn>',enter)
confirm_password.bind('<FocusOut>',leave)


def hide():
    print('Hide')
    openeye.config(file='eye1.png')
    confirm_password.config(show='*')
    eyebutton.config(command=show)
    
def show():
    openeye.config(file='eye.png')
    confirm_password.config(show='')
    eyebutton.config(command=hide)

openeye= PhotoImage(file='eye1.png')
eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show)
eyebutton.place(x=310,y=232)
    


sign = Button(frame,text="Confirm",bg='white',fg='#0048ba',border=0,command=lambda:openlogin())
sign.place(x=205,y=280)


sign = Button(frame,text="Login",bg='white',fg='green',border=0,command=lambda:openlogin())
sign.place(x=205,y=312)

o=Label(frame,text="Already have an account?",font=("Comic Sans Ms", 10),bg="white")
o.place(x=40,y=312)



window.mainloop()