'''
Write a script to concatenate all elements in a list into a string and print it.
List must be include both strings and integers and must be hardcoded.
'''

elements = ['Hello', 'i\'m', 28, 'years old']
elements = ' '.join(map(str, elements))
print(elements, end='.')
