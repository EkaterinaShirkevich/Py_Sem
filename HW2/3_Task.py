# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.

from unittest import result


len = int(input("Введите количество чисел: "))
ls = []
sum = 0
for i in range(1, len + 1):
    ls.append(round((1 + 1/len) ** len, 2))
print(ls)
for i in ls:
    sum += i
print(sum)

# без ыторого цикла, с созданием доп переменной result
# for i in range(1, len + 1):
#   result = ls.append(round((1 + 1/len) ** len, 2))
#   sum += result
#print(sum)
