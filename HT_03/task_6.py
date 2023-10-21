'''
Write a script to get the maximum and minimum value in a dictionary.
'''

values_dict = {
    'value1': 15,
    'value2': True,
    'value3': 256,
    'value4': (1, 2, 3),
    'value5': '72.8',
}
temp_list = [i for i in values_dict.values() if isinstance(i, int)]
print(min(temp_list))
print(max(temp_list))