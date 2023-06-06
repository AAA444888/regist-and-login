import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from regist_ import regist
import os
import pymysql
import db_dict
import user


def check():
    has=False
    name=name_text.get()
    idd=id.get()
    try:
        db_settings = db_dict.dict()
        conn = pymysql.connect(**db_settings)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM bmr_chart WHERE name = '{name}' AND id = '{idd}'")
        line = cursor.fetchall()
        print(line[0])
        conn.commit()
        conn.close()
        has=True
        user.user(name,idd)
    except Exception as e:
        conn.close()
        print(e)
    if has==False:
        text = tk.Label(wnd,text="login failed")
        text.place(relx=0.5,rely=0.5,anchor='n')
    else:
        text = tk.Label(wnd,text="login succes")
        text.place(relx=0.5,rely=0.5,anchor='n')

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("login")

namet = tk.Label(wnd,text='name')
namet.pack()
name_text = tk.Entry(wnd)
name_text.pack()

idt = tk.Label(wnd,text='id')
idt.pack()
id = tk.Entry(wnd)
id.pack()

button = tk.Button(wnd,text="log-in",underline=-1,command=check)
button.pack()
button = tk.Button(wnd,text="regist",underline=-1,command=regist)
button.place(relx=0.5,rely=0.8,anchor='n')

wnd.mainloop()