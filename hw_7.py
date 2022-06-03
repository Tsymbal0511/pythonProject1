#7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('hw7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Profit average - {prof_aver:.2f}')
    else:
        print(f'Profit average - missing. Everyone works at a loss')
    pr = {'Profit average': round(prof_aver)}
    profit.update(pr)
    print(f'Profit each company - {profit}')

with open('test.home_work.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Created file with extension json with the following content: \n '
          f' {js_str}')
