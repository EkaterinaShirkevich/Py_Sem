# 2. Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

max = 0
for i in range(5):
    a = int(input())
    if a > max:
        max = a
print(max)    