'''
Write a script that combines three dictionaries by updating the first one.
'''
# те ж саме (що і в task_3). Методи типів даних не вчив від слова зовсім.
# Гугли як робитьсбя апдейт словника іншим словником.
# Перероблено

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
temp_list = (dict_2, dict_3)
[dict_1.update(i) for i in temp_list]
print(dict_1)
