'''
Write a script which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
'''

numbers_list = input('Input comma-separated numbers: ').split(',')
numbers_tuple = tuple(numbers_list)
print(f'List: {numbers_list} \nTuple: {numbers_tuple}')
