from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime
from tkinter import ttk
import os

def choose_dir():
    dir_name=filedialog.askdirectory()
    l_path.delete(0,END)
    l_path.insert(0, dir_name)

def start_sort():
    c_pass=l_path.get()
    if c_pass:
        for folder, subfolder, files in os.walk(c_pass):
            for file in files:
                path= os.path.join(folder, file)
                mtime=os.path.getmtime(path)
                date=datetime.fromtimestamp(mtime)
                date=date.strftime("%Y-%m-%d")
                date_folder= os.path.join(c_pass,date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo("Success", "Сортировка завершена успешно")
    else: messagebox.showerror("No adress", "Проверьте введенный адрес")

root=Tk()
root['bg']="#963FD5"
root.title("Photo_sort")
root.geometry("400x90+400+200")
frame = Frame(root, bg="#680BAB", bd=10)
frame.pack(pady=5, padx=10, fill=X)
l_path=ttk.Entry(frame)
l_path.pack(side=LEFT, ipady=3,  expand=True, fill=X)
b_choose=ttk.Button(frame, text="Выберите папку", command=choose_dir)
b_choose.pack(side=LEFT, padx=10)
b_start=ttk.Button(root, text="Начать сортировку", command=start_sort)
b_start.pack(fill=X, padx=10)




root.mainloop()