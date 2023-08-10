from math import sqrt


class MyTriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'треугольник со сторонами {self.a}, {self.b}, {self.c}'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second


triangle = MyTriangle(2, 3, 5)
triangle_2 = MyTriangle(2, 3, 5)
triangle_3 = MyTriangle(5, 3, 2)
print(triangle == triangle_2)
print(triangle == triangle_2 == triangle_3)
print(triangle != triangle_2)
print('Обратите внимание на приставку не в функции. Реализовав один метод из пары(равно не равно),'
      ' второй Python попытается получить инвертируя значение')


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'

    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return _area

    def __lt__(self, other):
        return self.area() < other.area()

    def __hash__(self):
        return hash((self.a, self.b, self.c))


one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²')
print(f'{two} имеет площадь {two.area():.3f} у.е.²')
print(f'{one > two = }\n{one < two = }')
data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
result = sorted(data)
print('Далее создали список треугольников и отсортировали их. Визуальная проверка площадей подтверждает, '
      'что треугольники были упорядочены именно на основе их сравнения.')
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))

print('Простейшая реализация хэша')
triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)}
print(triangle_set)
print(', '.join(f'{hash(item)}' for item in triangle_set))
print('Сам дандер __hash__ возвращает результат вычисления хэша для кортежа из трёх элементов — длин сторон. ')
