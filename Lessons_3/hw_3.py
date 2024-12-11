#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает
# сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    print(f'The sum of the two largest arguments is: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Argument 1:')),
    int(input('Argument 2:')),
    int(input('Argument 3:')),
)
