from tkinter import *
import tkinter
root = Tk()
root.title("Signup form")
root.geometry("600x300")
root.configure(bg="#a83232")

title = Label(root, text ="SIGN UP", bg="#a83232", fg="white", font=("bold", 15))
title.place(x=250, y=20)

firstname = Label(root, text="FIRSTNAME", bg="#a83232", fg="White", font=("bold", 13))
firstname.place(x=100, y=80)
t_firstname = Entry()
t_firstname.place(x=230, y=80)

lastname = Label(root, text="LASTNAME", bg="#a83232", fg="White", font=("bold", 13))
lastname.place(x=100, y=110)
t_lastname = Entry()
t_lastname.place(x=230, y=110)

phonenumber = Label(root, text="PHONENUMBER", bg="#a83232", fg="White", font=("bold", 13))
phonenumber.place(x=100, y=140)
t_phonenumber = Entry()
t_phonenumber.place(x=230, y=140)

password = Label(root, text="PASSWORD", bg="#a83232", fg="White", font=("bold", 13))
password.place(x=100, y=170)
t_password = Entry(root,show="*")
t_password.place(x=230, y=170)

submit = Button(root, text="SIGNUP", bg="#003E53", fg="White", font=("bold", 13))
submit.place(x=250, y=200)
root.mainloop()