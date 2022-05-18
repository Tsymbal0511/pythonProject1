#4. Пользователь вводит целое положительное число.
num = int(input('Enter the number: '))
max = 0
while num != 0:
    cifr = num % 10
    if max < cifr:
        max = cifr
    num = num // 10
print(max)