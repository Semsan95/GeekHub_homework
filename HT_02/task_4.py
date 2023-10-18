'''
Write a script which accepts a <number> from user and then <number> times asks user for string input.
At the end script must print out result of concatenating all <number> strings.
'''

number = int(input('Input number: '))
count = 0
strings_list = []
while count != number:
    strings_list.append(input(f'Input string {count + 1}: '))
    count = count + 1
print(''.join(strings_list))
