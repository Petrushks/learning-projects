'''
В модуле присутствуют следующие атрибуты:

    Функции:
        file_check(checking) - открывает переданный в неё текстовый файл.
        main() - Функция для проверки модуля. 
'''


def file_check(checking):

    '''
    Функция открывает переданный в неё текстовый файл.

    Атрибуты функции:
        checking : str.

    Переменные:
        answer : str;
        file : str.

    Результат возвращается переменной answer.
        Переменная answer имеет два значения:
        1. Текстовая строка "FNF_ERROR", при указании неверного имени файла или пути к нему.
        2. Текстовая строка "Good", в противном случае.
    '''

    answer = 'Good'

    try:
        file = open(checking, 'r')
    except FileNotFoundError:
        answer = 'FNF_ERROR'

    return answer


def main():

    '''
    Функция для проверки модуля.
    '''

    RIGHT_FILENAME = 'FAHRENHEIT451_text.txt'
    INCORRECT_FILE_NAME = '1984.txt'

    print(f'Result : {file_check(RIGHT_FILENAME)}')
    print(f'Result : {file_check(INCORRECT_FILE_NAME)}')


if __name__ == '__main__':
    main()