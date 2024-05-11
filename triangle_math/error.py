'''
В модуле присутствуют следующие атрибуты:

    Функции:
        value_check(checking) - преобразует введённое значение в вещественный тип.
        infinit_check(checking) - проверяет величину значения.
        less_zero_error(checking) - проверяет величину значения.
        main() - функция для проверки работы модуля.
'''


def value_check(checking):

    '''
    Функция преобразует введённое значение в вещественный тип.

    Атрибуты функции:
        checking - переменная произвольного типа.

    Переменные:
        answer: str.

    Результат возвращается переменной answer.
        Переменная answer имеет два значения:
        1. Текстовая строка "VAL_ERROR", при ValueError;
        2. Текстовая строка "Good", в противном случае.
    '''
    
    answer = 'Good'

    try:
        float(checking)
    except ValueError:
        answer = 'VAL_ERROR'

    return answer


def infinit_check(checking: float):

    '''
    Функция проверяет величину значения: если оно больше допустимого, возвращает текстовую строку с кодом ошибки.

    Атрибуты функции:
        checking : int/foat.

    Переменные:
        answer : str;
        check : float.

    Результат возвращается переменной answer.
        Переменная answer имеет два значения:
        1. Текстовая строка "INF_ERROR", при OverflowError или inf/+inf/-inf/nan;
        2. Текстовая строка "Good", во всех прочих случаях.
    '''
    
    answer = 'Good'

    try:
        check = float(checking)**2 + float(checking)**2
    except OverflowError:
        answer = 'INF_ERROR'
    else:
        if (check == float('inf') or check == float('+inf') 
            or check == float('-inf') or check == float('nan')):
            answer = 'INF_ERROR'

    return answer


def less_zero_check(checking: float):

    '''
    Функция проверяет величину значения: если оно меньше или равно нулю, возвращает текстовую строку с кодом ошибки.

    Атрибуты функции:
        checking : int/float.

    Переменные:
        answer : str.

    Результат возвращается переменной answer.
        Переменная answer имеет два значения:
        1. Текстовая строка "LESS_ZERO_ERROR", при введении значения меньшего чем ноль;
        2. Текстовая строка "Good", в ином случае.
    '''
    
    answer = 'Good'

    if float(checking) <= 0:
        answer = 'LESS_ZERO_ERROR'

    return answer



def main():

    '''
    Функция для проверки работы модуля.
    '''
    
    print(f'32 - value result: {value_check(32)}')
    print(f'Three - value result: {value_check('Three')}')

    print()

    print(f'32 - infinit result: {infinit_check(32)}')
    print(f'100**200 - infinit result: {infinit_check(100**200)}')
    print(f'inf - infinit result: {infinit_check('inf')}')

    print()

    print(f'32 means : {less_zero_check(32)}')
    print(f'-32 means : {less_zero_check(-32)}')
    print(f'0 means : {less_zero_check(0)}')
    


if __name__ == '__main__':
    main()