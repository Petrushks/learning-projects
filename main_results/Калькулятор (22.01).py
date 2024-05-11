import tkinter
window = tkinter.Tk() # создаёт окно

window.title("Calculator")
window.geometry("400x400")

def add ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 + num_2 # д/з вместо принта сделать вставку ответа в окошко(которое еще создать нужно),"название текстового окна".insert(0,ответ)
    out = output.insert(0, answ)

def sub ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 - num_2 # д/з вместо принта сделать вставку ответа в окошко(которое еще создать нужно),"название текстового окна".insert(0,ответ)
    out = output.insert(0, answ)

def div ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 / num_2 # д/з вместо принта сделать вставку ответа в окошко(которое еще создать нужно),"название текстового окна".insert(0,ответ)
    out = output.insert(0, answ)

def mul ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 * num_2 # д/з вместо принта сделать вставку ответа в окошко(которое еще создать нужно),"название текстового окна".insert(0,ответ)
    out = output.insert(0, answ)

def ac ():
    output.delete(0, "end")

plus = tkinter.Button(window, text="+", command=add, height=2, width=3, foreground="green")
plus.place(x = 80, y = 120)
minus = tkinter.Button(window, text="-", command=sub, height=2, width=3, foreground="green")
minus.place(x = 110, y = 120)
devision = tkinter.Button(window, text=":", command=div, height=2, width=3, foreground="green")
devision.place(x = 140, y = 120)
multipliy = tkinter.Button(window, text="x", command=mul, height=2, width=3, foreground="green")
multipliy.place(x = 170, y = 120)
delite = tkinter.Button(window, text="AC", command=ac, height=2, width=3, foreground="green")
delite.place(x = 200, y = 120)


lb_1 = tkinter.Label(window, text="Enter") # метка ввода "Enter"
lb_1.place(x = 175.5, y = 0)

enter_1 = tkinter.Entry(window) # первое вводимое число
enter_1.place(x = 135.5, y = 20) 
enter_2 = tkinter.Entry(window) # второе вводимое число
enter_2.place(x = 135.5, y = 40)

lb_2 = tkinter.Label(window, text="Answer")
lb_2.place(x = 175.5, y = 60) # метка ответа "Answer"

output = tkinter.Entry(window) # окно вывода ответа
output.place(x = 135.5, y = 80)

window.mainloop() # обновляет значения окна
