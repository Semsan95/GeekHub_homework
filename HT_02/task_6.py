'''
Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False
'''

user_value = input('Input any value: ')
values_list = [1, 2, 'u', 'a', 4, True]
print(user_value in map(str, values_list))
