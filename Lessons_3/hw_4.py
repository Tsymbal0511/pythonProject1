# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
#Задание реализуйте в виде функции my_func(x, y).
#При решении задания нужно обойтись без встроенной функции возведения числа в степень.



def my_func(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result



print(f'Elevation degree option: '
      f'{my_func(int(input("Input number Х: ")), int(input("Input degree Y: ")))}')
