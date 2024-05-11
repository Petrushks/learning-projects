import time

opers = '+ - * /'.split()

def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mult(a, b):
    print(a * b)

def div(a, b):
    print(a / b)

def point(x):
    try:
        if '.' in x:
            return float(x)
        else:
            return int(x)
    except ValueError:
        print('Value Error!')


print('*' * 5, 'Consol calculator', '*' * 5)
time.sleep(2)
print()
print('To close the programm enter letter "q" or "Q"')
time.sleep(2)
print()
print('Enter the numbers or close the programm')
time.sleep(2)
print()
print('You can use following operetors: +, -, *, /')
time.sleep(2)
print()


while True:

    oper = input("Enter the operator:\n")
    if oper.lower() == 'q':
        break
    elif oper not in opers:
        print('Incorrect operator!')
        print()
        continue
    print()
    
    num_1 = input('The first number:\n')
    print()
    num_2 = input('The second number:\n')
    print()

    num_1 = point(num_1)
    num_2 = point(num_2)

    if oper == '+':
        try:
            add(num_1, num_2)
        except TypeError:
            print('This programm can add only numbers')
    elif oper == '-':
        try:
            sub(num_1, num_2)
        except TypeError:
            print('This programm can subtract only numbers')
    elif oper == '*':
        try:
            mult(num_1, num_2)
        except TypeError:
            print('This programm can multiply only numbers')
    elif oper == '/':
        try:
            div(num_1, num_2)
        except TypeError:
            print('This programm can divide only numbers')
        except ZeroDivisionError:
            print("We can't divide numbers on zero!")
        

