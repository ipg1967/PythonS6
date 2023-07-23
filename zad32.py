# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

minimum = int(input("Введите минимальный порог диапазона: "))
maximum = int(input("Введите верхний порог диапазона проверки: "))
array = [
    random.randint(1, 100) for i in range(20)
]  # какой то массив - в условии не оговорено
print('Массив создан:')
print(*array) # покажем созданный массив

# list = []
# for i in range(len(array)):
#     if minimum <= array[i] <= maximum:
#         list.append(i)
# print("индексы элементов массива в указанном диапазоне значений:")
# print(*list)

# то же но через компрехеншен лист
list_2 = [i for i in range(len(array)) if minimum <= array[i] <= maximum]
print(*list_2)
