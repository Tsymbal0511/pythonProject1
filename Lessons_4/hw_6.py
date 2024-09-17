#6. Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count
from itertools import cycle

a = int(input("Enter an integer numbers:"))
n = int(input("Count numbers:"))

print("Work of the first iterator")
cnt = 0
for i in count(a):
    if cnt < n:
        print(i)
        cnt += 1
    else:
        break

print("Work of the second iterator")
list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
cnt = 0
for j in cycle(list):
    if cnt < n:
        print(j)
        cnt += 1
    else:
        break
