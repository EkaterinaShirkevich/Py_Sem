# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

N = int(input("Введите число: "))
list = []
digit = 1
for i in range(2, N+2):
    list.append(digit)
    digit *= i
print(list)

# другой вариант:
# for i in range(num):
#   sum *= i + 1
#   print(sum, end=",")