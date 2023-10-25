'''
Write a Python program that demonstrates exception chaining.
Create a custom exception class called CustomError and another called SpecificError.
In your program (could contain any logic you want), raise a SpecificError,
and then catch it in a try/except block,
re-raise it as a CustomError with the original exception as the cause.
Display both the custom error message and the original exception message.
'''

class CustomError(Exception):
    pass

class SpecificError(Exception):
    pass

try:
    answer = input('What tastes better, pizza or sushi? ')
    if answer == 'pizza':
        print("You're right bro!")
    elif answer == 'sushi':
        raise SpecificError("Sushi can't be tastier than pizza!")
    else:
        print("Right answer is 'pizza' :P")
except SpecificError as e:
    raise CustomError('Total fail') from e
