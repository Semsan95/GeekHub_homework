'''
Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
Реалізуйте обчислення за допомогою генератора.
'''

def min_length(str_words):
    splitted_input = str_words.split(' ')
    return min(len(i) for i in splitted_input)

str_words = input('Введіть кілька слів через пробіл: ')
result = min_length(str_words)

print(result)
