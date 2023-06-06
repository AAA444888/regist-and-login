import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import db_dict

def regist():
    def insert(id,name,onthchoosen,weight,height,age):
        db_settings = db_dict.dict()
        conn = pymysql.connect(**db_settings)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM bmr_chart WHERE id = '{id}'")
        line = cursor.fetchall()
        if id==''or name=='' or onthchoosen=='' or weight=='' or height=='' or age=='':
            messagebox.showinfo('訊息','資料錯誤')
        elif len(line)>0:
            conn.close()
            messagebox.showinfo('訊息','資料重複')
        else:
            cursor.execute(f"INSERT INTO bmr_chart(num,id,name,gender,weight,height,age) VALUES (NULL,'{id}','{name}','{onthchoosen}','{weight}','{height}','{age}');")
            conn.commit()
            conn.close()
            messagebox.showinfo('訊息','新增成功')
            wnd.destroy()
            
    def submit():
        # t0 = tk.Label(wnd,text=id_text.get())
        # t0.place(relx=0.5,rely=0.75,anchor='n')
        # t1 = tk.Label(wnd,text=name_text.get())
        # t1.place(relx=0.5,rely=0.8,anchor='n')
        # t2 = tk.Label(wnd,text=onthchoosen.get())
        # t2.place(relx=0.5,rely=0.85,anchor='n')
        # t3 = tk.Label(wnd,text=wt_text.get())
        # t3.place(relx=0.5,rely=0.9,anchor='n')
        # t4 = tk.Label(wnd,text=ht_text.get())
        # t4.place(relx=0.5,rely=0.95,anchor='n')
        # t5 = tk.Label(wnd,text=age_text.get())
        # t5.place(relx=0.5,rely=1.0,anchor='n')
        insert(id_text.get(),name_text.get(),onthchoosen.get(),wt_text.get(),ht_text.get(),age_text.get())

    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("regist")
    
    idt = tk.Label(wnd,text='id')
    idt.pack()
    id_text = tk.Entry(wnd)
    id_text.pack()

    namet = tk.Label(wnd,text='name')
    namet.pack()
    name_text = tk.Entry(wnd)
    name_text.pack()

    gendert = tk.Label(wnd,text='gender')
    gendert.pack()
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('男生', '女生')
    onthchoosen.pack()

    wt = tk.Label(wnd,text='weight')
    wt.pack()
    wt_text = tk.Entry(wnd)
    wt_text.pack()

    ht = tk.Label(wnd,text='height')
    ht.pack()
    ht_text = tk.Entry(wnd)
    ht_text.pack()
    
    aget = tk.Label(wnd,text='age')
    aget.pack()
    age_text = tk.Entry(wnd)
    age_text.pack()

    button = tk.Button(wnd,text="finish",underline=-1,command=submit)
    button.pack()

    wnd.mainloop()