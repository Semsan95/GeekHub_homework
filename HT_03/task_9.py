'''
Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.
'''

first_year = int(input('Input first year: '))
last_year = int(input('Input last year: '))

for i in range(first_year, (last_year + 1)):
    if i % 4 == 0 and (i % 400 == 0 or i % 100 != 0):
        print(i)
