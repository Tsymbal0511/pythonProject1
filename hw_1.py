#1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

f = True

with open('test_home_work2.txt', 'w', encoding='utf-8') as f:
    #line = input('Enter text: ')
    while f:
        line = input('Enter text: ')
        if line != '': f.write(f'{line}\n')
        else: f = False




