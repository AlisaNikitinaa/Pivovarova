import datetime
from datetime import date

from pip._internal.resolution.resolvelib import found_candidates


def first():
    data1 = date.today()
    print(data1)
    data2 = date(2021, 12, 31)
    print(data2)
    d_year = data2.year
    print(d_year)
    return True

def operator():
    for i in [1, 2, 3]:
        print(i)
    for j in range(5):
        print(j)
    for letter in 'abcf':
        print(letter)
    return True

if __name__ == '__main__':
    operator()
    first()

def count_vowels(new_word: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for letter in new_word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    return found

if __name__ == '__main__':
    my_word = "hello"
    my_vowels = count_vowels(my_word)
    print(my_vowels)

def count_vowels2(new_word: str) -> dict:
    vowels = set('aeiouAEIOU')
    found = {}
    for letter in new_word:
        if letter in vowels:
            found.setdefault(letter, 0)
            found[letter] += 1
    return found

if __name__ == '__main__':
    my_word = "hello"
    found = count_vowels2(my_word)
    print('словарь=', found)
    print('переделаем словарь в список кортежей')
    found_tuple = found.items()
    print('кортеж', found_tuple)
    for key, value in found_tuple:
        print('letter', key, 'is found in letter', value)
