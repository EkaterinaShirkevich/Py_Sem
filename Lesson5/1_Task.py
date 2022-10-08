# 1. Создайте список из N натуральных чисел(0 до N), 
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].  
#    Найдите это число.

from secrets import choice


def fill_list(num: int):
    array = [i for i in range(num + 1)]
    array.remove(choice(array))
    return array

def check(array: list):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i-1]:
            return array[i] - 1
    return -1        

array = fill_list(int(input("Enter the number: ")))    
print(array)
print(check(array))