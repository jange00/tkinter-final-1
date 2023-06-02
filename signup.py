# from tkinter import*
# from PIL import Image,ImageTk
# from tkinter import messagebox,messagebox

# window = Tk()
# window.title("Login")
# window.geometry("1000x500")
# window.resizable(False,False)
# window.config(bg="white")
# img0= PhotoImage(file="b5.png")
# label1=Label(window, image= img0)
# label1.pack(fill=X)




# frame=Frame(window,width=460,height=300,bg='white',borderwidth=3)
# frame.place(x=40,y=10)
# a=Label(frame,text="Welcome to Bikebreeze",font=("Comic Sans MS", 17, 'bold'),fg='blue')
# a.place(x=62,y=20)

# # def login():
# #     v = Email.get()
# #     print(v)
# #     l = Password.get()
# #     print(l)
# #     window.destroy()
    
# # fEmail=1
# # fpassword = 1

# # def enter(event):
# #     print(Email.get())
   
# #     global fEmail
# #     if(fEmail == 1):
# #         if(Email.get()  == "Email"):
# #             Email.delete(0,END)
# #             return
# #         fEmail = 2

# # def leave(event):
# #     if Email.get()=='':
# #         Email.insert(0,"Email")
# def enter(event):
#     Email.delete(0,'end')
    
# def leave(event):
#     a=Email.get()
#     if a=='':
#         Email.insert(0,'Email')


# # Email=Entry(frame,text="Email",bg='white',fg="black",font=("Comic Sans Ms", 10, "bold"))
# Email=Entry(frame,text="Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
# Email.place(x=140,y=80)
# Email.insert(0,"Email")

# z=Frame(frame,width=180,height=2,bg='black')
# z.place(x=80,y=150)  

# Email.bind("<FocusIn>",enter) #that it becomes the active element that can receive user input.
# Email.bind('<FocusOut>',leave)  #meaning that it is no longer the active element that can receive user input.


# # def enter (event):
# #     global fpassword
# #     if(fpassword == 1):
# #         if(Password.get() == "Password"):
# #             Password.delete(0,END)
# #             return
# #         fpassword = 2
    
# # def leave(event):
# #     if Password.get() == "":
# #         Password.insert(0,"Password")


# # Password=Entry(frame,text="Password",bg='white',fg="black",show='*',font=("Comic Sans Ms", 10, "bold"))
# Password=Entry(frame,text="Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show="*")
# Password.place(x=140,y=130)

# y=Frame(frame,width=180,height=2,bg='black')
# y.place(x=80,y=100)  
         
# Password.insert(2,"Password")
# Password.bind('<FocusIn>',enter) #that it becomes the active element that can receive user input.
# Password.bind('<FocusOut>',leave)  #meaning that it is no longer the active element that can receive user input.


# sign = Button(frame,text="     Login     ",bg="green",command=lambda:login())
# sign.place(x=178,y=170)

# forget =Button(frame,text='Forgot Password',bg='white',fg='blue')
# forget.place(x=100,y=230)

# signup = Button(window,text="Sign Up")
# signup.place(x=400,y=400)


# window.mainloop()





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
password.place(x=130,y=195)

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
confirm_password.place(x=130,y=240)

v=Frame(frame,width=250,height=2,bg='black')
v.place(x=80,y=260)

confirm_password.insert(1,'Confirm Password')
confirm_password.bind('<FocusIn>',enter)
confirm_password.bind('<FocusOut>',leave)



#show password functionalities for passwords
def show():
        if showw.get()==1:
            password.config(show="")
        else:
            password.config(show='*')


showw=IntVar()
b1=Checkbutton(frame,text="Show",bg='white',fg='black',border=0,onvalue=1,variable=showw,offvalue=0, command=show)
b1.place(x=310,y=190)

def show2():
        
        if showww.get()==1:
            confirm_password.config(show='')
        else:
            confirm_password.config(show='*')
            
 
showww=IntVar()
b2=Checkbutton(frame,text="Show",bg='white',fg='black',border=0,onvalue=1,variable=showww,offvalue=0, command=show2)
b2.place(x=310,y=232)
    


sign = Button(frame,text="Confirm",bg='white',fg='#0048ba',border=0,command=lambda:openlogin())
sign.place(x=170,y=278)


sign = Button(frame,text="Login",bg='white',fg='green',border=0,command=lambda:openlogin())
sign.place(x=205,y=312)

o=Label(frame,text="Already have an account?",font=("Comic Sans Ms", 10),bg="white")
o.place(x=40,y=312)



window.mainloop()