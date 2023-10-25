'''
Create a custom exception class called NegativeValueError.
Write a Python program that takes an integer as input
and raises the NegativeValueError if the input is negative.
Handle this custom exception with a try/except block and display an error message.
'''

class NegativeValueError(Exception):
    pass

try:
    int_input = int(input('Enter any integer: '))
    if int_input < 0:
        raise NegativeValueError("You are too negative! >:(")
except NegativeValueError as e:
    print('NegativeError:', e)
else:
    print('Good job! Be Positive! ;)')