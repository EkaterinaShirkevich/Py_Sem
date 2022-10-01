# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample

def ls_form(count, find_num2):
    if count < 0:
        return("Bad choice")
    ls = random.sample(range(count*2), count)
    print(ls)
    if find_num2 in ls:
        return("Yes")
    return("No")    

num1 = input("Enter the number: ")
num2 = input("Enter the number: ")
print(ls_form(num1, num2))

# from random import sample

# def magic(count, find_num2):
#     if count < 0:
#         return "Все плохо"
#     ls = random.sample(range(count * 2), count)
#     print(ls)

#     if find_num2 in ls:
#         return "Yes"
#     return "No"


# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# print(magic(num1, num2))
