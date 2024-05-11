import random, time

a = time.time()

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''','''
+---+
o   |
    |
    |
   ===''','''
+---+
o   |
|   |
    |
   ===''','''
 +---+
 o   |
/|   |
     |
    ===''','''
 +---+
 o   |
/|\  |
     |
    === ''','''
 +---+
 o   |
/|\  |
/    |
    ===''','''
 +---+
 o   |
/|\  |
/ \  |
    ===''']

words = 'аист акула бабуин барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козёл койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орёл осёл панда паук питон попугай пума сёмга скунс собака сова тигр тритон тюлень утка форель хорёк черепаха ястреб ящерица'.split()

def get_random_word(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    word_index= random.randint(0, len(wordList))
    return wordList[word_index]

def display_board(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Заменяет пропуски отгаданными буквами.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами.
        print(letter, end=' ')
    print()

def get_guess(alreadyGuessed):
    # Возвращает букву, введённую игроком. Эта функция проверяет, что игрок ввёл только одну букву и ничего более.
    while True:
        print('Введите букву:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess

def play_again():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
    print('Хотите сыграть ещё? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    # Позволяет игроку ввести букву.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # Проверяет, выйгрыл ли игрок.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f'Да! Секретное слово - {secret_word}! Вы угадали!')
            game_is_done = True

            if game_is_done:
                if play_again():
                    missed_letters = ''
                    correct_letters = ''
                    secret_word = get_random_word(words)
                    game_is_done = False
                else:
                    out = int(time.time() - a)
                    print(f'Общее время игры составило: {out} сек.')
                    break

    else:
        missed_letters = missed_letters + guess
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f'Вы исчерпали все попытки!\nНе угадано букв: {len(missed_letters)} и угадано букв: {len(correct_letters)}. Было загадано слово: {secret_word}.')
            game_is_done = True

            # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
            if game_is_done:
                if play_again():
                    missed_letters = ''
                    correct_letters = ''
                    game_is_done = False
                    secret_word = get_random_word(words)
                else:
                    out = int(time.time() - a)
                    print(f'Общее время игры составило: {out} сек.')
                    break
