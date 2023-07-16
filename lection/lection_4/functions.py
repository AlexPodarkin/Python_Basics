def no_mutable(x):
    x += 1
    print(f"arg func = {x}")
    return x


a = 42
print(f"in main{a =}")
z = no_mutable(a)
print(f"{a = }\t{z =}")


# Если по ссылке передали неизменяемый объект, мы не можем его изменить (int, float, tuple, frozen... )
# если мы по ссылке передали изменяемый объект (list, set, dict... ) то изменения внутри функции затронут внешний объект

def func_1(a=0):
    print(a)


print(func_1())
# значение по умолчанию a = 0
print(func_1(5))


# В качестве значения по умолчанию нельзя указывать изменяемы типы: списки, словари, множества и т.п.!


def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(n):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(new_list)
other_list = from_one_to_n(7)
print(other_list)


# так рекомендуется работать с сылочными типами (list, set, dict... )


def mean(args):
    return sum(args) / len(args)


print(mean([5, 5, 5]))
# print(mean(5, 5, 5)) Type ERROR

def mean(*args):
    return sum(args) / len(args)


print(mean(*[5, 5, 5]))
print(mean(5, 5, 5))
# *args любое кол-во позиционных аргументов (поэтому мы распаковываем в 1-ом случае *[5, 5, 5])
# *args превращается в картеж

def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f"по предмету {key} получена оценка {value}")


school_print(химия=5, физика=5, математика=5)
# При написании своих функций стоит помнить о возможности сочетать позиционные
# и ключевые переменные, специальные символы разделители / и *, а также
# переменные *args и **kwargs.
# **kwargs превращается в словарь

LIMIT = 1_000

def func_3(x, y):
    result = x * y / LIMIT
    return result


print(func_3(123, 159))
# тот самый допустимый пример применения переменной\константы внутри функции Python, но только на чтение (НЕ ЗАПИСЬ !)
# константа неизменяемый тип данных
