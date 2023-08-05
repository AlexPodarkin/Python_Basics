import time
from functools import wraps, cache


def dict_cache(func):
    new_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in new_dict:
            print('Запуск функции ! ')
            new_dict[args] = func(*args, **kwargs)
        return new_dict[args]

    return wrapper


@dict_cache
def factorial(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


print(factorial(5))
print(factorial(4))
print('Эти значения мы получили из кеша !')
print(factorial(5))
print(factorial(4))

print('\n Декоратор с параметрами')


def measure_time(count=1):
    def real_decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            list_time = []
            result = None
            for i in range(count):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                list_time.append((stop - start, result))
            print('результат замера скорости выполнения и результат ->', list_time)
            return result

        return wrapper

    return real_decorate


@measure_time(2)
def factorial_2(n):
    """Функция для вычисления факториала"""
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


print('результат ->', factorial_2(5))
print('результат ->', factorial_2(5))
print('имя функции: ', factorial_2.__name__)
print('описание функции: ', factorial_2.__doc__)


print('\nНаписать декоратор счетчик вызова функций')

def count_func(func):
    count_1 = 0
    wraps(func)

    def wrapper(*args, **kwargs):
        nonlocal count_1
        count_1 += 1
        result = func(*args, **kwargs)
        return 'ответ -> ', result, f'количество вызовов функции = {count_1}'

    return wrapper


@count_func
def factorial_3(n):
    """Функция для вычисления факториала"""
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


print(factorial_3(5))
print(factorial_3(5))
print(factorial_3(5))
