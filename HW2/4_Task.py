#Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).

num = int(input("Enter the value of N: "))
n1 = int(input("Position one: "))
n2 = int(input("Position two: "))

nums_list = list(range(-num, num + 1))
print(nums_list)

len_list = len(nums_list)

if len_list >= n1 > 0 and len_list >= n2 > 0:
    print(nums_list[n1 - 1] * nums_list[n2 - 1])
else:
    print("There are no values for these indexes.")