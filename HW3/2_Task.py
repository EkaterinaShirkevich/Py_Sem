# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

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

def pairs_mult(list_nums: list):
    ls = []
    for i in range(len(list_nums) // 2):
        mult = list_nums[i] * list_nums[len(list_nums) - i - 1]
        ls.append(mult)
    if len(list_nums) % 2 != 0:
        ls.append(list_nums[len(list_nums) // 2])
    return ls    

list = list_random(int(input("Введите количество чисел для списка: ")))
print(f"Ваш список: {list}") 
print(f"Результат: {pairs_mult(list)}")        
