import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import regist
import os

def check():
    has=False
    if os.path.exists("user.txt"):
        with open("user.txt",mode='r',encoding='UTF-8') as file:
            lines=file.readlines()
            for line in lines:
                line_obj = line.split()
                if line_obj[0]==name_text.get() and line_obj[4]==password.get():
                    has=True
                    text = tk.Label(wnd,text="login succes")
                    text.place(relx=0.5,rely=0.5,anchor='n')
    if has==False:
        text = tk.Label(wnd,text="login failed")
        text.place(relx=0.5,rely=0.5,anchor='n')

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("login")

namet = tk.Label(wnd,text='name')
namet.pack()
name_text = tk.Entry(wnd)
name_text.pack()

passwordt = tk.Label(wnd,text='password')
passwordt.pack()
password = tk.Entry(wnd)
password.pack()

button = tk.Button(wnd,text="finish",underline=-1,command=check)
button.pack()
button = tk.Button(wnd,text="regist",underline=-1,command=regist.regist)
button.place(relx=0.5,rely=0.8,anchor='n')

wnd.mainloop()