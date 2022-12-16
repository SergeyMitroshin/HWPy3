# ДОП2 
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=114&id_problem=702

import random



size = int(input('Введите число n: '))
li = random.sample(range(size),size)
for i in range(len(li)):
    print (li[i], end = '  ')
li.reverse()
print ()
for i in range(len(li)):
    print (li[i], end = '  ')