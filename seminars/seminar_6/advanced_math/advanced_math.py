"""Two advanced mathematical operations.
Integer division and exponentiation."""
__all__ = ['div', 'exp']
_BEGINNING = 0
_CONTINUATION = 1


def div(*args):
    res_1 = args[_BEGINNING]
    for item_1 in args[_CONTINUATION:]:
        res_1 //= item_1
    return res_1


def exp(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
        res **= item
    return res


if __name__ == '__main__':
    print(f'{div(42, 4) = }')
    print(f'{exp(2, 4, 6, 8) = }')
