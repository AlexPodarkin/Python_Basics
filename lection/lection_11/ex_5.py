print('Обработка атрибутов')


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    """Строка return object.__getattribute__(self, item) является
            обязательной. Без неё может возникнуть ошибка переполнения стека."""

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

    # def __getattr__(self, item):
    #     return None

    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


print('Получение значения атрибута, __getattribute__')
a = Vector(2, 4)
# __getattribute__
# print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
print(f'{a = }')

print('Присвоение атрибуту значения, __setattr__')
# __setattr__
# a.z = 73  # AttributeError: У нас вектор на плоскости, а не в пространстве
a.x = 3
print(f'{a = }')

print('Обращение к несуществующему атрибуту,__getattr__')
# __getattr
# print(a.z)

print('Удаление атрибута, __delattr__')
print('При попытке удалить атрибут командой del можно использовать дандер __delattr__для изменения логики.')
a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(a)
# print(f'{a = }, {a.s = }')

print('Функции setattr(), getattr() и delattr()')
# Разница лишь в том, что метод
# реагирует на событие в коде, а функцию вы вызываете в тот момент, когда вам это нужно.
# ● setattr(object, name, value) — аналог object.name = value
# ● getattr(object, name[, default]) — аналог object.name or default
# ● delattr(object, name) — аналог del object.name
