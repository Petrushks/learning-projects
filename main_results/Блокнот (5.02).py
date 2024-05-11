from tkinter import *


import tkinter.filedialog as fd

import tkinter.messagebox as mb

root = Tk()

root.geometry ("300x240")
root.title("Text book")

strings = Text(root)
strings.place(x = 0, y = 0, relwidth=1, relheight=1)

menu_main = Menu(root, background="grey")
root.configure(menu=menu_main)

file_name = "Untitled"
opened_file = Label(root, text=file_name)
opened_file.place(relx=0, rely=1, anchor="sw")

def new_file():
    global file_name
    if mb.askokcancel(title="New file creation", message="Are you sure? Unsaved data will delete!"):
        file_name = "Untitled"
        strings.delete(1.0, "end")
        opened_file["text"]=file_name


def open_file ():
    global file_name
    file_name = fd.askopenfilename()
    strings.delete(1.0, "end")
    with open(file_name, encoding="utf-8") as text:
        strings.insert(1.0, text.read())
    opened_file["text"]=file_name

def save_as():
    global file_name
    file_name = fd.asksaveasfilename()
    with open(file_name, "w", encoding="utf-8") as text:
        text.write(strings.get(1.0, "end"))
    opened_file["text"]=file_name

def save():
    global file_name
    if file_name == "Untitled":
        save_as()
    else:
        with open(file_name, "w", encoding="utf-8") as text:
            text.write(strings.get(1.0, "end"))
    opened_file["text"]=file_name

menu_file = Menu(menu_main)
menu_main.add_cascade(label="File", menu=menu_file)

new_file_image = PhotoImage(file="C:/Users/proko/OneDrive/Рабочий стол/Шпаргалки Python/new_file.gif")
menu_file.add_command(label="New file", image=new_file_image, compound="right", command=new_file)

open_file_image = PhotoImage(file="C:/Users/proko/OneDrive/Рабочий стол/Шпаргалки Python/open_file.gif")
menu_file.add_command(label="Open file", image=open_file_image, compound="right", command=open_file)

save_image = PhotoImage(file="C:/Users/proko/OneDrive/Рабочий стол/Шпаргалки Python/save_file.gif")
menu_file.add_command(label="Save", image=save_image, compound="right", command=save)

menu_file.add_command(label="Save as", image=save_image, compound="right", command=save_as)


root.mainloop()