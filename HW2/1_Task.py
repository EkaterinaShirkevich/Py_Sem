# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.

num = input("Введите вещественное число: ")
num = float(num)*10**len(num)
print(num)
sum = 0
while num > 0:
    sum += num%10
    num //= 10
print(int(sum))

