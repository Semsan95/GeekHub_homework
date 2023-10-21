'''
Write a script that combines three dictionaries by updating the first one.
'''

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
temp_list = (dict_2, dict_3)
[dict_1.update(i) for i in temp_list]
print(dict_1)