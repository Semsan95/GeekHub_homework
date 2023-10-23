'''
Write a script to get the maximum and minimum value in a dictionary.
'''
# почитай як визначається макимальн і мінімальне значення
# для рядків (це не те ж саме що довжина), списків, кортежів і т.д.
# Даю підказку - можливо доведеться створити кілька "груп" результатів в залежності від порявняння
# (бо ти ж не можеш порівняти наприклад число з рядком).
# Перероблено

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
