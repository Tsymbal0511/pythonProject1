#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#Вывести каждое слово с новой строки.
#Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

my_string = input('enter the string: ')
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {element} {my_word [element]}")
    else:
        print(f" {element} {my_word [element] [0:10]}")