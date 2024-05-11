'''
В модуле присутствуют следующие атрибуты:

    Функции:
        diam_circle_square(size) - проводит вычислениe площади окружности на основе величины её диаметра.
        diam_circle_length(size) - проводит вычислениe длины окружности на основе величины её диаметра.
        rad_circle_square(size) - проводит вычислениe площади окружности на основе величины её радиуса.
        rad_circle_length(size) - проводит вычислениe длины окружности на основе величины её радиуса.
        main() - функция для проверки работы модуля.

    Импортируемые:
        pi - константа модуля math.

    Константы:
        NUMBER_PI : float.
'''


from math import pi


NUMBER_PI = round(pi, 2)


def diam_circle_square(size: float):

    '''
    Функция проводит вычислениe площади окружности на основе величины её диаметра.

    Атрибуты функции:
        size : int/float.

    Переменные:
        square : float.

    Результат возвращается переменной square.
    '''

    square = (size // 2) * pow(NUMBER_PI, 2)

    return round(square, 2)


def diam_circle_length(size: float):

    '''
    Функция проводит вычислениe длины окружности на основе величины её диаметра.

    Атрибуты функции:
        size : int/float.

    Переменные:
        length : float.

    Результат возвращается переменной length.
    '''
    
    length = size * NUMBER_PI

    return round(length, 2)


def rad_circle_square(size: float):

    '''
    Функция проводит вычислениe площади окружности на основе величины её радиуса.

    Атрибуты функции:
        size : int/float.

    Переменные:
        square : float.

    Результат возвращается переменной square.
    '''
    
    square = size * pow(NUMBER_PI, 2)

    return round(square, 2)


def rad_circle_length(size: float):

    '''
    Функция проводит вычислениe длины окружности на основе величины её радиуса.

    Атрибуты функции:
        size : int/float.

    Переменные:
        length : float.

    Результат возвращается переменной length.
    '''
    
    length = 2 * NUMBER_PI * size

    return round(length, 2)

def main():

    '''
    Функция для проверки работы модуля.
    '''

    print(type(pi))

    print(f'Circle square from diameter : {diam_circle_square(6)}')
    print(f'Circle length from diameter : {diam_circle_length(6)}')

    print()

    print(f'Circle square from radius : {rad_circle_square(3)}')
    print(f'Circle length from radius : {rad_circle_length(3)}')


if __name__ == '__main__':
    main()