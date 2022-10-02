# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

def string_with_nums(string_val):
    for i in string_val:
        if not i.replace("-", "").isdigit():
            return []
    return string_val        

def min_max_demo(val):
    art = string_with_nums(val)
    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []  

print(min_max_demo(input("Enter numbers in string: ").split()))         
