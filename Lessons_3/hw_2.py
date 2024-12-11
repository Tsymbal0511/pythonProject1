#2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Осуществить вывод данных о пользователе одной строкой.

def personal_data(name, surname, year_of_birth, city, email, phone):
    return print(f'Name: {name} Surname: {surname} Year of birth: {year_of_birth}'
                 f'Current city: {city} Email: {email} Phone: {phone}')


personal_data(name=input('Name: '), surname=input('Surname: '), year_of_birth=input('Year of birth: '),
              city=input('Current city: '), email=input('email: '), phone=input('phone: '),
)



