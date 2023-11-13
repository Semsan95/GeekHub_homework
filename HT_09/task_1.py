'''
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного,
   а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори.
   Через декілька ітерацій - відбувається зміна кольорів -
   логіка така сама як і в звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
'''

import time

light1 = 'Green'
light2 = 'Yellow'
light3 = 'Red'
iterations = int(input('Введіть кількість ітерацій: '))

for i in range(iterations):
    if i % 12 in [0, 1, 2, 3]:
        print(f'{light3:<8}{light1}')
    elif i % 12 in [4, 5]:
        print(f'{light2:<8}{light3}')
    elif i % 12 in [6, 7, 8, 9]:
        print(f'{light1:<8}{light3}')
    else:
        print(f'{light2:<8}{light3}')
    time.sleep(1)


