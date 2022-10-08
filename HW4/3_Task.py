# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]


import random


def print_list(len: int):
    if len < 0:
        print("Длина списка не может быть отрицательной.")
        return []
    else:
        ls = []
        for i in range(1, len + 1):
            ls.append(random.randrange(1, len, 1))
        return ls

def non_rep_same_order(ls: list):
    new_list = []
    for i in ls:
        count = ls.count(i)
        if count == 1:
            new_list.append(i)       
    return new_list              

first_list = print_list(int(input("Введите длину списка: ")))
print(f"Ваш список: {first_list}")
print(f"Список неповторяющихся элементов: {non_rep_same_order(first_list)}")    

# лучший вариант решения с помощью словаря - подходит для больших объемов
# и немного оптимизированное формирование списка
# def list_rand_nums(count: int):
#     if count > 0:
#         print("Negative valur of numbers!")
#         return []
#     list_nums = []
#     for i in range(count):
#         list_nums.append(random.randrange(count))
#     return list_nums

# def uniq_el(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums, 0) # формировние словаря - все значения встанут как ключи,а ключи уникальные и неизменяеиые
#     for i in list_nums:
#         my_dict[i] += 1
#     for k in my_dict:
#         if my_dict[k] == 1:
#             result.append(k)
#     return result                       