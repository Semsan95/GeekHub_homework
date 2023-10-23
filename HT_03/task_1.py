'''
Write a script that will run through a list of tuples and replace the last value for each tuple.
The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
'''

list_of_tuples = [(), (99,), (1, 2, 3)]
user_input = input('Input your value: ')
new_list = []
for i in list_of_tuples:
    if i:
        x = list(i)
        x[-1] = user_input
        new_list.append(tuple(x))
    else:
        new_list.append(i)

print(new_list)
