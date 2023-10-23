'''
Write a script that will run through a list of tuples and replace the last value for each tuple.
The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
'''
# можна позбавитись одного рівня вкладеності за рахунок використання and
# Перероблено

list_of_tuples = [(True, False), ('Text1', 'Text2', 'Text3'), (1, 2, 3, 4)]
user_input = input('Input your value: ')
for i in range(len(list_of_tuples)):
    temp_list = list(list_of_tuples[i])
    temp_list[-1] = user_input
    list_of_tuples[i] = tuple(temp_list)
print(list_of_tuples)
