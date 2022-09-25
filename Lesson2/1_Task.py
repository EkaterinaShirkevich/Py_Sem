# Программа принимает на вход число N и выдаёт последовательность из N членов

N = int(input("Введите N: "))
num = 1
for i in range(N):
    print(num, end=" ")
    num*= -3
