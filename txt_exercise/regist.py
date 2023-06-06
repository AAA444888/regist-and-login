import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def regist():
    def insert(name_text,phone_num,onthchoosen,gmail,password):
        with open("user.txt",mode='a+',encoding='UTF-8') as file:
            file.write(name_text.get()+" "+phone_num.get()+" "+onthchoosen.get()+" "+gmail.get()+" "+password.get()+"\n")
        print("註冊成功")
    def submit():
        text1 = tk.Label(wnd,text=name_text.get())
        text1.pack()
        text2 = tk.Label(wnd,text=phone_num.get())
        text2.pack()
        text3 = tk.Label(wnd,text=onthchoosen.get())
        text3.pack()
        text4 = tk.Label(wnd,text=gmail.get())
        text4.pack()
        text5 = tk.Label(wnd,text=password.get())
        text5.pack()
        insert(name_text,phone_num,onthchoosen,gmail,password)

    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("regist")

    namet = tk.Label(wnd,text='name')
    namet.pack()
    name_text = tk.Entry(wnd)
    name_text.pack()

    phonet = tk.Label(wnd,text='phone number')
    phonet.pack()
    phone_num = tk.Entry(wnd)
    phone_num.pack()


    sext = tk.Label(wnd,text='sex')
    sext.pack()
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('男生', '女生')
    onthchoosen.pack()

    gmailt = tk.Label(wnd,text='gmail')
    gmailt.pack()
    gmail = tk.Entry(wnd)
    gmail.pack()

    passwordt = tk.Label(wnd,text='password')
    passwordt.pack()
    password = tk.Entry(wnd)
    password.pack()

    button = tk.Button(wnd,text="finish",underline=-1,command=submit)
    button.pack()

    wnd.mainloop()