'''
Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
'''

class User:
    users_amount = 0

    def __init__(self):
        User.users_amount += 1

user1 = User()
user2 = User()
user3 = User()
print(User.users_amount)