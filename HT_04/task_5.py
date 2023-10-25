'''
Create a Python program that repeatedly prompts the user
for a number until a valid integer is provided.
Use a try/except block to handle any ValueError exceptions,
and keep asking for input until a valid integer is entered.
Display the final valid integer.
'''

while True:
    try:
        user_input = int(input('Please input a valid integer: '))
    except ValueError as e:
        print(e, 'this value is total invalid.')
    else:
        print('Your valid integer is:', user_input)
        break