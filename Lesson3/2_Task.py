# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from cgitb import reset
from itertools import count
from random import choices
from unittest import result

def form_word_list(count, source): # кол-во эл-тов и исходное слово - последовательность
    result = []
    for i in range(count):
        temp = choices(source, k = 3)
        result.append("".join(temp))
    return result

def find_second_encounter(word, words_list):
    if words_list.count(word)>1:
        first_encounter = words_list.index(word)
        print(f"второе вхождение: {words_list.index(word, first_encounter + 1)}")
    else:
        print("-1")

count, source = int(input()), input()
words = form_word_list(count, source)
print(words)
4
find_second_encounter(input(), words)




