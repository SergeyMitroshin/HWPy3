# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random 

size = int(input('Введите количество элементов: '))
li = []
for i in range(size):
    li.append(round(random.uniform(0,10),2))
print (li)

min = li[0] - li[0] // 1
max =  min
for i in range (len(li)):
    x = li[i] - li[i] // 1
    if x < min:
        min = x
    if x > max:
        max = x
dif = max - min
print(round(dif,2))
