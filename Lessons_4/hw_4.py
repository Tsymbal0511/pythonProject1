#4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
#Сформируйте итоговый массив чисел, соответствующих требованию.
#Элементы выведите в порядке их следования в исходном списке.
#Для выполнения задания обязательно используйте генератор.

import random

n = int(input('Input length of the list: '))
my_list = []
for i in range(n):
    my_list.append(random.randint(0, 10))
print("Initial List Items:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("List elements that do not have duplicates:\n", new_list)
