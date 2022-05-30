#2.Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

result_list = []
list = [int(i) for i in input('Enter a list of numbers: ').split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print('Source List: ', list)
print('A list whose elements are greater than the previous one: ', result_list)
