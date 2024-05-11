'''
В модуле присутствуют следующие атрибуты:

    Функции:
        value_inp(TEXT) - запрашивает ввод значения длины у пользователя.
        command_inp(TEXT) - запрашивает у пользователя ввод команды.
        geometry_choiсe(TEXT) - запрашивает у пользователя ввод одного из заданных значений.
        main() - обеспечивает текстовый интерфейс для взаимодействия с пользователем.

    Импортируемые:
        Пространство имён модуля error.
        Пространство имён модуля solution.
        Пространство имён модуля talking_text.
'''

from error import *
from solution import *
from talking_text import *


def value_inp(TEXT):

    '''
    Функция запрашивает ввод значения длины у пользователя (до тех пор, пока не будет введено значение верного типа).

    Атрибуты функции:
        TEXT : str.

    Переменные:
        number : str/float;
        result : str.

    Результат возвращается переменной number.
    '''
    
    print(TEXT)

    number = input()

    result = value_check(number)
    if result == 'VAL_ERROR':
        number = value_inp(ErrorResponde.INCORRECT_VALUE_TEXT)
    else:
        result = less_zero_check(number)
        if result == 'LESS_ZERO_ERROR':
            number = value_inp(ErrorResponde.LESS_ZERO_TEXT)
        else:
            result = infinit_check(number)
            if result == 'INF_ERROR':
                number = value_inp(ErrorResponde.INFINIT_ERROR_TEXT)

    return float(number)
            


def command_inp(TEXT):

    '''
    Функция запрашивает у пользователя ввод команды (до тех пор, пока не будет введена одна из доступных команд).

    Атрибуты функции:
        TEXT : str.

    Переменные:
        command : str;
        begin_flag : bool.

    Результат возвращается переменной begin_flag.
    '''
    
    print(TEXT)

    command = input(Commands.COMMAND_INPUT_TEXT)

    match command:
        case 'start':
            begin_flag = True
        case 'exit':
            begin_flag = False
        case _:
            begin_flag = command_inp(Commands.INCORRECT_COMMAND_TEXT)

    return begin_flag


def geometry_choiсe(TEXT):

    '''
    Функция запрашивает у пользователя ввод одного из заданных значений.

    Атрибуты функции:
        TEXT : str.

    Переменные:
        command : str;
        answer : str.

    Результат возвращается переменной answer.
    '''

    print(TEXT)

    command = input()

    match command:
        case '1':
            answer = 'diam'
        case '2':
            answer = 'rad'
        case _:
            answer = geometry_choiсe(Commands.INCORRECT_CODE_TEXT)

    return answer


def main():

    '''
    Функция обеспечивает текстовый интерфейс для взаимодействия с пользователем.

    Переменные:
        flag : bool;
        command : bool;
        figure : str;
        length : float.
    '''
    
    print(Politeness.EXPLANATION_TEXT)

    flag = True

    while flag:

        command = command_inp(Commands.BEGINING_COMMAND_TEXT)
        
        match command:
            case True:
                figure = geometry_choiсe(Commands.GEOMETRY_COMMAND_TEXT)
                match figure:
                    case 'diam':
                        length = value_inp(Politeness.INPUT_TEXT)
                        print(f'\nДлина окружности равна: {diam_circle_length(length)}')
                        print(f'Площадь круга составляет: {diam_circle_square(length)}\n')
                    case 'rad':
                        length = value_inp(Politeness.INPUT_TEXT)
                        print(f'\nДлина окружности равна: {rad_circle_length(length)}')
                        print(f'Площадь круга составляет: {rad_circle_square(length)}\n')
            case False:
                print()
                print(Politeness.GOODBY_TEXT)
                flag = False


if __name__ == '__main__':
    main()