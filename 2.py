# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

size = int(input('Введите количество элементов: '))
li = random.sample(range(size),size)
print (li)
sum = []
if len(li) % 2 == 0:
    for i in range(len(li) // 2):
        sum.append(li[i] * li[len(li) - i - 1])
else:
    for i in range(len(li) // 2 + 1):
        sum.append(li[i] * li[len(li) - i - 1])
print (sum)