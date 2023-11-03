'''
Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення.
'''


def user_input(num1, num2):
    try:
        start = int(num1)
        end = int(num2)
        return start, end
    except ValueError:
        raise ValueError('Please enter integer value.')


def prime_list(num1, num2):
    start, end = user_input(num1, num2)
    prime_numbers = []

    for number in range(start, end + 1):
        if number in [0, 1]:
            continue
        elif number in [2, 3]:
            prime_numbers.append(number)
            continue

        check = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                check = False
                break
        if check:
            prime_numbers.append(number)

    return prime_numbers

num1 = input('Enter first number: ')
num2 = input('Enter last number: ')

print(prime_list(num1, num2))
