'''Write a script which accepts decimal number from user and converts it to hexadecimal.'''

decimal = hex(int(input('Input decimal number: ')))[2:]
print('Your number in hexadecimal is:', decimal.upper())
