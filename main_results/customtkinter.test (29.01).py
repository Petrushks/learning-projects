import customtkinter
root = customtkinter.CTk()

customtkinter.set_appearance_mode("Dark")

root.geometry("400x260")
root.title("Calculator")
#root.wm_attributes("-alpha", 0.7) # делает окно прозрачным
root.configure()

def add ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 + num_2 
    out = output.insert(0, answ) # выводит ответ

def sub ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 - num_2 
    out = output.insert(0, answ) # выводит ответ

def div ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 / num_2 
    out = output.insert(0, answ) # выводит ответ

def mul ():
    num_1 = int(enter_1.get()) # получает значение первого вводимого числа
    num_2 = int(enter_2.get()) # получает значение второго вводимого числа
    enter_1.delete(0, "end")
    enter_2.delete(0, "end")
    output.delete(0, "end")
    answ = num_1 * num_2 
    out = output.insert(0, answ) # выводит ответ

def ac ():
    output.delete(0, "end")

plus = customtkinter.CTkButton(root, text="+", command=add) # кнопка сложения
plus.place(x = 62.75, y = 150)

minus = customtkinter.CTkButton(root, text="-", command=sub) # кнопка вычитания
minus.place(x = 208.25, y = 150)

division = customtkinter.CTkButton(root, text=":", command=div) # кнопка деления
division.place(x = 62.75, y = 185)

multiplication = customtkinter.CTkButton(root, text="x", command=mul) # кнопка умножения
multiplication.place(x = 208.25, y = 185)

delete = customtkinter.CTkButton(root, text="AC", command=ac) # кнопка очистки ответа
delete.place(x = 135.5, y = 220)


lb_1 = customtkinter.CTkLabel(root, text="Enter") # метка ввода "Enter"
lb_1.place(x = 190, y = 0)

enter_1 = customtkinter.CTkEntry(root) # первое вводимое число
enter_1.place(x = 135.5, y = 20) 
enter_2 = customtkinter.CTkEntry(root) # второе вводимое число
enter_2.place(x = 135.5, y = 60)

lb_2 = customtkinter.CTkLabel(root, text="Answer")
lb_2.place(x = 185, y = 90) # метка ответа "Answer"

output = customtkinter.CTkEntry(root) # окно вывода ответа
output.place(x = 135.5, y = 110)

root.mainloop()
