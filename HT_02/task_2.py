'''
Write a script which accepts two sequences of comma-separated colors from user.
Then print out a set containing all the colors from color_list_1 which are not present in color_list_2
'''

color_list_1 = input('Input first sequence: ').split(',')
color_list_2 = input('Input second sequence: ').split(',')
color_set = set(color_list_1) - set(color_list_2)
print(color_set)