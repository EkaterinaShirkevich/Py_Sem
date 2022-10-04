# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Негафибоначчи
def negative_fibo(num: int):
    a, b = 1, 1
    ls = []
    for i in range(num):
        ls.append(a)
        ls.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return ls

print(*negative_fibo(int(input("Введите число: "))))        