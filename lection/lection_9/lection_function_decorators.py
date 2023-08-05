import time
from functools import wraps


def add_one_str(str_1):
    def wrapper(str_2):
        print(f'{str_1}, {str_2}')

    return wrapper


hi = add_one_str('Hello')
by = add_one_str('Good bye')
hi('Alex !')
by('Alex !')
print(f'{hi} \n{by}')
print('адреса в оперативной памяти разные, а названия указывают на оригинал')


def add_one_str(a):
    text = ''

    def add_two_str(b):
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
# Что более важно - неизменяемый тип данных у строки text.
# Без добавления строчки кода nonlocal text была бы получена ошибка

print('Простой декоратор без параметров')


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(f'время работы функции {et - st} сек')
        return result

    return wrapper


factorial_dec = test_time(factorial)
print(factorial_dec(5))
print(f'{factorial_dec.__name__ = }')

print("В языке Python есть более элегантная возможность создания декораторов")


def time_now(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("запуск функции, время : ", time.ctime())
        result = func(*args, **kwargs)
        print("окончание работы функции, время : ", time.ctime())
        return result

    return wrapper


@test_time
@time_now
def factorial_decor(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print('Ответ -> ', factorial_decor(4))

print('Тут я сделал все ручками :) -> ', test_time(time_now(factorial))(5))
