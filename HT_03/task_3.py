'''
Write a script to concatenate following dictionaries to create a new one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}
'''

'''dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
temp_list = (dict_1, dict_2, dict_3)
new_dict = {}
[new_dict.update(i) for i in temp_list]
print(new_dict)'''

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
temp_list = (dict_1, dict_2, dict_3)
new_dict = {}
[new_dict.update(i) for i in temp_list]
print(new_dict)