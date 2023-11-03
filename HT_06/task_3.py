'''
Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
'''


def is_prime(number):
    if number in range(0, 1001):
        if number in [0, 1]:
            return False
        elif number in [2, 3]:
            return True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


number = int(input('Enter number between 0 to 1000: '))
print(is_prime(number))
