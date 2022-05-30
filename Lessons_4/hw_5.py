#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
#В список должны войти чётные числа от 100 до 1000 (включая границы).
#Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("List of even numbers in a range [100..1000]:\n", list)
print("The product of all elements of a list:\n", reduce(lambda x,y: x*y, list))
