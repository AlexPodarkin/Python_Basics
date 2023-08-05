import random


def game(guess=10, number_of_attempts=3):
    if guess > 10:
        guess = random.randint(1, 100)
    if number_of_attempts > 10:
        number_of_attempts = random.randint(1, 10)

    def wraps():
        nonlocal guess
        nonlocal number_of_attempts
        while number_of_attempts > 0:
            inp_user = int(input(f'Какое число я загадал(кол-во попыток {number_of_attempts})? -> '))
            if inp_user > guess:
                print('Мое число меньше !')
            elif inp_user == guess:
                print("'Поздравляю !!! Ты угадал '")
                return None
            else:
                print('Мое число больше')
            number_of_attempts -= 1

    return wraps


game_cl = game(10, 5)
game_cl()
