#2. Пользователь вводит время в секундах.

time_sec = int(input('Enter the number: - '))

hour = time_sec// 3600
time_sec %= 3600
min = time_sec // 60
time_sec %= 60

print(str(hour) + ":" + str(min) + ":" + str(time_sec))