# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. (ДОП)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):

    if n == 0 or n == 1:
        return n
    if n == -1:
        return -n
    if n < 0:
        return round(fib(abs(n)) * (-1)**(n + 1))
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input('Введите количество чисел: '))
for i in range(-n, n + 1):
    print(fib(i), end='  ')
print()