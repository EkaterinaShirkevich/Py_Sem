# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

from random import sample


def form_words(count: int, source_set: str):
    words = []
    for i in range(count):       
        new_set = sample(source_set, len(source_set))
        words.append(''.join(new_set))
    return ' '.join(words)   

def del_set(words: str) -> str:
    to_del = input("Введите комбинацию, которую нужно удалить: ")
    return words.replace(to_del, "")

count = int(input("Введите количество желаемых комбинаций: "))
set = input("Введите буквы, из которых будут составлены комбинации: ")
words = form_words(count, set)
print(words)
print(del_set(words))
    

