"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
"""
_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1


def add(*args):
    res_1 = _START_SUM
    for item_1 in args:
        res_1 += item_1
    return res_1


def sub(*args):
    res_2 = args[_BEGINNING]
    for item_2 in args[_CONTINUATION:]:
        res_2 -= item_2
    return res_2


def mul(*args):
    res_3 = _START_MULT
    for item_3 in args:
        res_3 *= item_3
    return res_3


def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res /= item
    return res
