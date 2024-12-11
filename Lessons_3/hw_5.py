#5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
#Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Enter numbers separated by spaces: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'Sum {general_sum}')

    if stop_flag:
        break
