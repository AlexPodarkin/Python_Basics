import fractions


def common_div(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = (a + b)
    return res


# функция для нахождения НОД


num1, denom1 = list(map(int, input("Введите 2 числа для составления 1-ой дроби(пр: a/b) -> ").split('/')))
num2, denom2 = list(map(int, input("Введите 2 числа для составления 2-ой дроби(пр: a/b) -> ").split('/')))

if denom1 == denom2:
    print('Сумма дробей = {} / {}'.format(num1 + num2, denom1))
else:
    cd = int(denom1 * denom2 / common_div(denom1, denom2))
    rn = int(cd / denom1 * num1 + cd / denom2 * num2)
    g2 = common_div(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print('\tСумма дробей = {} / {}'.format(n, d) if n != d else n)

# произведение дробей
e = num1 * num2
f = denom1 * denom2
print(f"\tПроизведение дробей = {e}/{f}")

f_1 = fractions.Fraction(num1, denom1)
f_2 = fractions.Fraction(num2, denom2)
print(f"Проверка: \n\tСумма дробей = {f_1 + f_2} \n\tПроизведение дробей = {f_1 * f_2}")
