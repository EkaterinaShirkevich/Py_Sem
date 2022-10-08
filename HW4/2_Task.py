# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]

import math


def fact (num: int):
    if num <= 0:
        return ("Error (try to enter correct number)")
    ls = []
    while num % 2 == 0:
           ls.append(2)
           num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            ls.append(i)
            num //= i
    if num > 2:
        ls.append(num)           
    return ls
    
num = int(input("Enter the number: "))
print(f"Factorize for {num} is {fact(num)}") 


# оптимизация для длинных списков, чтобы не перебирать весь в каждом цикле
# pr_fact = []
# di = 2 # делитель
# while num > 1:
#     if num % di == 0:
#         pr_fact.append(di)
#         num /= di
#     else:
#         di += 1   
# return pr_fact