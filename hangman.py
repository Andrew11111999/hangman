import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # случайным образом выбирает что-то из списка
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # буквы в слове
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    used_letters = set()  # о чём догадался пользователь

    lives = 6

    # корректировка пользовательского ввода
    while len(word_letters) > 0 and lives > 0:
        # используемые буквы
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('У тебя осталось', lives, 'жизней. Вы использовали эти буквы: ', ' '.join(used_letters))

        # какое текущее слово является (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Текущее слово: ', ' '.join(word_list))

        user_letter = input('Угадай букву: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # если что-то не так, это отнимает жизнь
                print('Буквы нет в слове.')

        elif user_letter in used_letters:
            print('Вы уже использовали этот символ. Пожалуйста попробуйте снова.')
        else:
            print('Недопустимый символ. Пожалуйста попробуйте снова.')

    if lives == 0:
        print('Извините вы проиграли. Слово было: ', word)
    else:
        print('Поздравляю! Вы угадали слово:', word, '!!')


hangman()
