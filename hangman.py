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

