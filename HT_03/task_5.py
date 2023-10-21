'''
Write a script to remove values duplicates from dictionary.
Feel free to hardcode your dictionary.
'''

my_dict = {
    'int': 15,
    'float': 2.17,
    'str': 'Geekhub',
    'list': (1, 2, 3),
    'str_2': 'Geekhub',
    'boolean': True,
}
temp_dict = {}
for key, value in my_dict.items():
    if value not in temp_dict.values():
        temp_dict[key] = value
my_dict = temp_dict
print(my_dict)
