'''
Write a script which accepts a <number> from user and generates dictionary in range <number>
where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}
'''

user_input = int(input('Input number: '))
user_dict = {}
for i in range(user_input + 1):
    user_dict[i] = i * i
print(user_dict)
