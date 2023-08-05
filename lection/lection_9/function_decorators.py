import time

print("Декораторы функций\n")


def func_decor(func):
    def wrapper(*args, **kwargs):
        print("Делает что то до функции")
        result = func(*args, **kwargs)
        print("Делает что то после функции")
        return result

    return wrapper


def func_1(arg):
    print(f"работа функции func_1 | arg = {arg}")
    return 'успешно'


func_in_decor = func_decor(func_1)
print(func_in_decor('аргумент'))

print("\nможно использовать как замер скорости работы функций")


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'-> время работы функции {dt} сек')
        return result

    return wrapper


def add_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return "add_list успех"


add_list_dec = test_time(add_list)
print(add_list_dec(1_000_000))

func_1_dec = test_time(func_1)
print(func_1_dec('arg'))

print("      -=Декоратор с параметрами=-")


def decor_with_par(param="параметр декоратора по умолчанию"):
    def decor_test_time(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            st = time.time()
            print("> замер времени")
            result = func(*args, **kwargs)
            et = time.time()
            dt = et - st
            print(f'> время работы функции {dt} сек')
            print(f'параметр декоратора = {param}')
            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decor_test_time


@decor_with_par(param='5')
def test_func():
    """Описание функции test_func"""
    print("РАБОТА")
    return "-> то что вернула функция"


print(test_func())
print("\nКак решить проблему имен ?")
print(test_func.__name__)
print(test_func.__doc__)
# при помощи wrapper.__name__ = func.__name__ и wrapper.__doc__ = func.__doc__ мы решили проблему имен
# есть встроенный декоратор в библиотеке - from functools import wraps
# @wraps(func) - в аргументе указать имя функции
