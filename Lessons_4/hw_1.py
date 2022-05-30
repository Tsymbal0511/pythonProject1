#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
#Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
#Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

def simple_calc():
    x = float(input('Enter the number of work hours: '))
    y = float(input('Enter the amount of wages for 1 hour : '))
    c = float(input('Specify the amount of the bonus - '))
    return x * y + c
print(f'The salary was: {simple_calc() }')
