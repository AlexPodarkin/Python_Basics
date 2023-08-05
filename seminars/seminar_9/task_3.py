import json
from functools import wraps


def dec_json_save(func):
    new_dict = {}

    def wrapper(*args, **kwargs):
        if args not in new_dict:
            new_dict[args] = None
        result = func(*args, **kwargs)
        new_dict[args] = result
        print(new_dict)

        return result

    return wrapper


@dec_json_save
def func_1(a, num=0):
    res = a + num
    return res


func_1(2)
func_1(2, 3)
func_1(3, 3)
func_1(4, 4)
func_1(5, 5)

print([str(x) for x in (3, 6)])

