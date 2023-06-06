import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import second

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("first")
def show():
    print(name_text.get())
    text1 = tk.Label(wnd,text=name_text.get())
    text1.pack()
name_text = tk.Entry(wnd)
name_text.pack()
add = tk.Button(wnd,text="Add Data",underline=-1,command=show)
add.pack()
add_sec = tk.Button(wnd,text="Add Data",underline=-1,command=second.ab)
add_sec.pack()
text = tk.Label(wnd,text='second_line')
text.place(relx=0.5,rely=0.5,anchor='n')
n = tk.StringVar()
onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
onthchoosen['values'] = ('男生', '女生')
onthchoosen.place(relx=0.6,rely=0.3,anchor="n")
close = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
close.pack()
messagebox.showinfo('訊息','哈囉！')
wnd.mainloop()