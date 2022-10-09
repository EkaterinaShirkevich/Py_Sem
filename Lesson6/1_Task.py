# 1. Напишите программу вычисления арифметического
#    выражения заданного строкой. Используйте операции +,-,/,*
#    приоритет операций стандартный. Добавьте скобки, приоритет операций меняется.
actions = {
    "^": lambda x, y: float(x) ** float(y),
    "*": lambda x, y: float(x) * float(y),
    "/": lambda x, y: float(x) / float(y),
    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y)
}

def calc(str):
    ls = str.split()
    prior = {"(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}
    priznak = []   # приоритеты {"(": 1, ")": 1, "*": 2}
    for i in ls:
        if i in prior:
            priznak.append(prior[i])
        else:
            priznak.append("")

    cur = priznak[1]
    for i, tmp in enumerate(priznak):
        if isinstance(tmp, int) and tmp < cur:
            curi = i
            cur = tmp
    curoperval = actions[ls[curi]](ls[curi - 1], ls[curi + 1])
    #print(curoperval)
    del ls[curi - 1: curi + 2]
    ls.insert(curi - 1, curoperval)
    print(ls)

    return priznak



str = '5 / 2 + 2'
print(calc(str))
