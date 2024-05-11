'''
В модуле присутствуют следующие атрибуты:

    Импортируемые:
        read_head() - метод модуля solution;
        file_check() - метод модуля error;
        Пространство имён модуля talking_text.

    Функции:
        file_inp() - запрашивает ввод имени файла или пути к нему;
        main() - обеспечивает текстовый интерфейс для работы с пользователем.

'''


from solution import read_head
from error import file_check
from talking_text import *


def file_inp(TEXT):

    '''
    Функция запрашивает ввод имени файла или пути к нему.

    Атрибуты:
        TEXT : str.

    Переменные:
        file_name : str;
        result : str.

    Результат возвращается переменной file_name.
    '''

    print(TEXT)

    file_name = input()

    result = file_check(file_name)
    if result == 'FNF_ERROR':
        print(ErrorResponde.INCORRECT_FILE_NAME)
        file_name = file_inp(Politeness.AGAIN_TEXT)
        return file_name
    else:
        return file_name



def main():

    '''
    Функция обеспечивает текстовый интерфейс для работы с пользователем.

    Переменные:
        flag : bool;
        command : str;
        name_of_file : str;
        text : list.

    '''

    print(Politeness.EXPLANATION_TEXT)

    flag = True

    while flag:

        print(Commands.BEGINING_COMMAND_TEXT)
        print(Commands.EXIT_COMMAND_TEXT)

        command = input(Commands.COMMAND_INPUT_TEXT)

        command = command.lower()

        match command:
            case 'start':
                name_of_file = file_inp(Politeness.INPUT_TEXT)
                text = read_head(name_of_file)
                for i in range(len(text)):
                    print(text[i], end='')
            case 'exit':
                print(Politeness.GOODBY_TEXT)
                flag = False
            case _:
                print(Commands.INCORRECT_COMMAND_TEXT)


if __name__ == '__main__':
    main()
