# ДОП2 
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=702

import random

def printlist (list):
    for i in range(len(list)):
        print (list[i], end = '  ')
    print ()

size = int(input('Введите число n: '))
li = random.sample(range(10),size)
printlist(li)
li.reverse()
printlist(li)