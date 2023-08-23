import logging

logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    format='{name}: {asctime} {levelname} {lineno} -> {msg}',
                    style='{',
                    level=logging.INFO)

x, y = map(int, input('Введите два целых числа через пробел: ').split())


def log_deco(func):
    def wrapper(x, y):
        try:
            logging.info(f'Func {func.name} Args: {x}  {y} Res: {func(x, y)}')
        except ZeroDivisionError:
            logging.error('ZeroDivisionZero')

    return wrapper


@log_deco
def log_div(x, y):
    return x / y


@log_deco
def log_mult(x, y):
    return x * y


log_div(x, y)
log_mult(x, y)
