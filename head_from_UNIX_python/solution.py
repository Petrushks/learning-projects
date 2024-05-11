'''
В модуле присутствуют следующие атрибуты:

    Функции:
        read_head(text_file) - осуществляет прочтение первых десяти строк текстового файла.
        main() - Функция для проверки модуля.

    Константы:
        FILENAME : str.
'''

FILENAME = 'C:\\code\\class_work_8\\ex_one\\FAHRENHEIT451_text.txt'

def read_head(text_file):
    '''
    Функция осуществляет прочтение первых десяти строк текстового файла.

    Атрибуты функции:
        text_file : str.

    Переменные:
        file : _io.TextIOWrapper;
        strings : list.

    Результат возвращается переменной strings.
    '''

    strings  = []

    with open(text_file, 'r') as file:
        for i in range(10):
            strings.append(next(file))
    
    return strings


def main():

    '''
    Функция для проверки модуля.
    '''

    print('Testing...\n')
    print(read_head(FILENAME))
    print('All tests are over.')


if __name__ == '__main__':
    main()