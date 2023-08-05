from random import randint


def main(func):
    def wrapper(*args):
        return func(*args)

    return wrapper


def try_to_guess(upper_limit, find_try):
    lower_limit = 1
    num = randint(lower_limit, upper_limit)
    print(f'Угадай число от {lower_limit} до {upper_limit}.\n')
    tmp = find_try

    while find_try > 0:
        guess_try = int(input('Введи число: '))
        find_try -= 1
        if guess_try < num:
            print('У меня больше.')
        if guess_try > num:
            print('У меня меньше.')
        if guess_try == num:
            print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
            return
    else:
        print(f'\nНе угадал! Я загадал {num}.')


try_to = main(try_to_guess)
try_to(10, 10)
