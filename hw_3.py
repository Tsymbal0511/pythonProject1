#3. Создать текстовый файл (не программно).
#Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('hw3.txt', 'r', encoding='utf-8') as f:
    my_list = f.read().split('\n')

sal = []
poor = []

print(my_list)
for i in my_list:
    i = i.split()
    if float(i[1]) < 20000:
       poor.append(i[0])
    sal.append(i[1])
print(f'Less salary 20.000 {poor}, average salary {sum(map(float, sal)) / len(sal)}')
