#5. Запросите у пользователя значения выручки и издержек фирмы.
revenue = int(input('Введите значение прибыли: '))
costs = int(input('Введите значение издержек: '))
if revenue < costs:
    print('Убыток')
elif revenue > costs:
    print('прибыль')
else:
    print('фирма выходит в 0')

#6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
revenue = int(input('Введите значение прибыли: '))
costs = int(input('Введите значение издержек: '))

if revenue < costs:
    print('Убыток')
elif revenue > costs:
    profit = revenue - costs
    print('прибыль: ', profit)
    people = int(input('Ввдите количество работников: '))
    print(profit / people)
else:
    print('фирма выходит в 0')