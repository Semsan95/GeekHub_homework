'''
Write a script which accepts a <number> from user
and print out a sum of the first <number> positive integers.
'''

number = int(input('Input number: '))
numbers_list = list(range(1, number + 1))
print(sum(numbers_list))
