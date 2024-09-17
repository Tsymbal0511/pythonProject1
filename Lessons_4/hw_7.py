#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор.
#Функция вызывается следующим образом: for el in fact(n).
#Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial

def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

n = int(input('Input count of numbers: '))

for el in factorial_gen(n):
    print(el)
