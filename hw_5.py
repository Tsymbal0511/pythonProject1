#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
    try:
        with open('hw5.txt', 'w+') as file_obj:
            line = input('Enter numbers separated by spaces \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('File error')
    except ValueError:
        print('Wrong number. I/O error')
summary()
