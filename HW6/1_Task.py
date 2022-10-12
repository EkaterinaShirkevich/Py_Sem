# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample


def list_random(len: int):
    if len < 0:
        print("Длина списка не может быть отрицательной.")
        return []
    else:
        ls = sample(range(start, fin), len)
        return ls
print("Введите промежуток, в котором будут выбраны числа:")
start = int(input("От "))
fin = int(input("До "))  

list = list_random(int(input("Введите количество чисел для списка: ")))
print(list)

new_list = [list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]
print(new_list) 