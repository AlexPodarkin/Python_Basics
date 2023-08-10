from decimal import Decimal

print('Математика и логика в классах')

print('Сложение через __add__ Создадим класс вектор и научим вектора складываться')


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Vector({self.a}, {self.b})'

    def __add__(self, other):
        res = self.a + other.a
        res_2 = self.b + other.b
        return Vector(res, res_2)


v_1 = Vector(1, 1)
v_2 = Vector(2, 2)
v_3 = v_1 + v_2
print(v_1, v_2, v_3, sep=" | ")


class MulStr(str):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __mul__(self, other):
        words = self.split()
        result = other.join(words)
        return MulStr(result)


mul = MulStr('I love Python')
mul_2 = MulStr(' (^.^) ')
mul_3 = mul * mul_2
print(f'Рукописный метод умножения строк {mul_3} тпи: {type(mul_3)}')

print('Вычисление процентов вместо нахождения остатка от деления, __imod__')


class Money:

    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)
print('Важно! Не забывайте return self при работе с in place дандер методами.')
