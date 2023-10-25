'''
Create a Python script that takes an age as input.
If the age is less than 18 or greater than 120,
raise a custom exception called InvalidAgeError.
Handle the InvalidAgeError by displaying an appropriate error message.
'''

class InvalidAgeError(Exception):
    pass

try:
    age = int(input('Enter age over 18: '))
    if age not in range(18, 121):
        raise InvalidAgeError('Age is not appropriate.')
except InvalidAgeError as e:
    print('AgeError:', e)
else:
    print('The entered age is:', age)
