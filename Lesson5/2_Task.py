# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.

from random import choices


def get_list(n: int):
    return choices(range(n*2), k = n)

def find_list(ls: list):
    res = []
    for i in range(len(ls)):
        cur = ls[i]
        cur_list = [cur]
        for k in range(i, len(ls)):
            if ls[k] > cur:
                cur_list.append(ls[k])
                cur = ls[k]
        if len(cur_list) > 1:
            res.append(cur_list)
    return res                

n = int(input("Enter the number: "))
array = get_list(n)
print(array)
print(find_list(array))    