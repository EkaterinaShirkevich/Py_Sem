# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#  дробной части элементов

from random import uniform


def list_rand_nums(len: int):
    ls = []
    if len <= 0:
        print("Длина списка не может быть отрицательной.")
        return [0.0]
    for i in range(len):
        ls.append(round(uniform(1, len), 2))
    return ls

def dif_max_min(list_nums: list):
    max = list_nums[0] % 1
    min = list_nums[0] % 1
    for i in range(1,len(list_nums)):
        num = round(list_nums[i] % 1, 2)
        if num > max:
            max = num
        elif num < min:
            min = num
    dif = round(max - min, 2) 
    print(f"Min: {min}, Max: {max}, Difference: {dif}")  
    return dif         



list = list_rand_nums(int(input("Введите длину списка: ")))        
print(f"Ваш список: {list}") 
print(f"Результат: {dif_max_min(list)}")        
     
