# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


x = int(input ('Введите число: '))

def DecToBin(a):
    if a == 0:
        print(a)
        return
    elif a != 1:
        DecToBin(a // 2)
    print(a % 2, end='')

DecToBin(x)
print ()