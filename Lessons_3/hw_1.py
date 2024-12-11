#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def calculator(num1, num2):
    if num2 == 0:
        print('Division by 0 is not possible')
    else:
        return num1 / num2

a = int(input('First number: '))
b = int(input('Second number: '))

result = calculator(a, b)
print(result)
