'''
Write a script to get the maximum and minimum value in a dictionary.
'''

values_dict = {
    'value1': 1,
    'value2': 15,
    'value3': 256,
    'value4': {1, 2, 3},
    'value5': (4, 5, 6, 7),
    'value6': [8, 9, 10, 11, 12],
    'value7': 'Apple',
    'value8': 'Banana',
    'value9': 'Orange',
    'value10': True,
    'value11': False,
    'value12': 562.8,
}
words = []
numbers = []
iterable = []
for i in values_dict.values():
    if isinstance(i, (int, float)):
        numbers.append(i)
    elif isinstance(i, str):
        words.append(i)
    else:
        iterable.append(list(i))

print('Words max value:', max(words))
print('Words min value:', min(words))
print('Numbers max value:', max(numbers))
print('Numbers min value:', min(numbers))
print('Iterable max value:', max(iterable))
print('Iterable min value:', min(iterable))
