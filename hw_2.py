#2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('hw2.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    print(f'Amount of Lines {len(line)}')
    for index, value in enumerate(line, 1):
        number_of_words = len(value.split())
        print(f'Line {index} will keep {number_of_words} words')
