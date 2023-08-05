import json


def json_saver(func):
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}.json', 'a') as file:
            temp_dict = {'args': args}
            temp_dict.update(kwargs)
            result = func(*args, **kwargs)
            temp_dict['result'] = result
            json.dump(temp_dict, file, indent=3, ensure_ascii=False)
        return result

    return wrapper


@json_saver
def factorial_2(n=0):
    """Функция для вычисления факториала"""
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


print(factorial_2(n=5))
