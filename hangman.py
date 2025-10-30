import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) # случайным образом выбирает что-то из списка
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # буквы в слове
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # о чём догадался пользователь

    # корректировка пользовательского ввода
    user_letter = input('Угадай букву').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('Вы уже использовали этот символ. Пожалуйста попробуйте снова.')
    else:
        print('Недопустимый символ. Пожалуйста попробуйте снова.')


user_input = input('Напечатайте что-нибудь')
print(user_input)

