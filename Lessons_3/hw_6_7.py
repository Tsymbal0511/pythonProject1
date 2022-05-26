#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(text):
    return text.title()

def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output = []
print(int_func(input('Enter a word: ')))

for word in input('Enter a string with words separated by spaces: ').split(' '):
    output.append(my_title(word))

print(f'The line looks like this: {" ".join(output)}')