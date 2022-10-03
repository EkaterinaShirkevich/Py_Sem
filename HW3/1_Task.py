# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

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

def sumnums_oddpos(list_nums: list):
    sum = 0
    for i in range(0, len(list_nums), 2):
        sum += list_nums[i]
    return sum     

list = list_random(int(input("Введите количество чисел для списка: ")))
print(list) 
print(sumnums_oddpos(list))  

