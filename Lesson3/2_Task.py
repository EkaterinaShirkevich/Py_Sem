# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import choices

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

count, source = int(input("Enter count of combinations: ")), input("Enter original sequence: ")
words = form_word_list(count, source)
print(words)
find_second_encounter(input("Enter desired sequence: "), words)




