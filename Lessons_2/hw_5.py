#5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
#У пользователя нужно запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [5, 4, 3, 2, 1]
print(f'Rating - {my_list}')
digit = int(input('Enter number (000 - output) '))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f'current list - {my_list}')
    digit = int(input('Enter number (000 - output) '))