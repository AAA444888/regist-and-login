import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import db_dict
import update_

def user(name,id):
    def delete():
        db_settings = db_dict.dict()
        conn = pymysql.connect(**db_settings)
        cursor = conn.cursor()
        try:
            cursor.execute(f"DELETE FROM bmr_chart WHERE name='{name}' AND id='{id}'")
            conn.commit()
            conn.close()
            messagebox.showinfo('訊息','刪除成功')
            wnd.destroy()
        except Exception as e:
            conn.close()
            print(e)
            
    def update():    
        def up():
                gender = onthchoosen.get()
                height = height_text.get()
                weight = weight_text.get()
                age = age_text.get()
                db_settings = db_dict.dict()
                conn = pymysql.connect(**db_settings)
                cursor = conn.cursor()
                cursor.execute(f"UPDATE bmr_chart SET gender='{gender}',weight = '{weight}',height='{height}',age='{age}' WHERE name='{name}' AND id='{id}'")
                conn.commit()
                conn.close()
                messagebox.showinfo('訊息','更新完畢')
                wnd.destroy()
        wnd = tk.Tk()
        wnd.geometry("400x400")
        wnd.title("Update Data")
        
        sext = tk.Label(wnd,text='請選擇欲更新的性別:')
        sext.place(relx=0.3,rely=0.3,anchor='n')
        n = tk.StringVar()
        onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
        onthchoosen['values'] = ('男生', '女生')
        onthchoosen.place(relx=0.7,rely=0.3,anchor='n')
        
        weightt = tk.Label(wnd,text='請輸入欲更新的體重(單位: 公斤):')
        weightt.place(relx=0.3,rely=0.5,anchor='n')
        weight_text = tk.Entry(wnd)
        weight_text.place(relx=0.7,rely=0.5,anchor='n')

        heightt = tk.Label(wnd,text='請輸入欲更新的身高(單位: 公分):')
        heightt.place(relx=0.3,rely=0.4,anchor='n')
        height_text = tk.Entry(wnd)
        height_text.place(relx=0.7,rely=0.4,anchor='n')
        
        aget = tk.Label(wnd,text='請輸入欲更新的年齡:')
        aget.place(relx=0.3,rely=0.6,anchor='n')
        age_text = tk.Entry(wnd)
        age_text.place(relx=0.7,rely=0.6,anchor='n')
        
        button = tk.Button(wnd,text="update",underline=-1,command=up)
        button.place(relx=0.5,rely=0.7,anchor='n') 
                    
        button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
        button.place(relx=0.7,rely=0.7,anchor='n')
        
        wnd.mainloop()
            
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("User")
    
    button = tk.Button(wnd,text="update",underline=-1,command=update)
    button.pack()
    button = tk.Button(wnd,text="delete account",underline=-1,command=delete)
    button.place(relx=0.5,rely=0.8,anchor='n')