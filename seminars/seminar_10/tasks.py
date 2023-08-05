# Задание 1
# создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * pi * self.radius


circle = Circle(1)
print(f"{circle.get_area()}, {circle.get_perimetr()}")


# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def per(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b


rectangle_1 = Rectangle(2)
print(f'периметр 1: {rectangle_1.per()}')
print(f'площадь 1: {rectangle_1.square()}')
rectangle_2 = Rectangle(1, 2)
print(f'периметр 2: {rectangle_2.per()}')
print(f'площадь 2: {rectangle_2.square()}')


# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, lastname, sex, age):
        self.name = name
        self.lastname = lastname
        self.sex = sex
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.lastname}, возраст: {self.__age}'

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.lastname}, возраст: {self.__age}'

    def det_age(self):
        return self.__age


pers_1 = Person("Alex", "Smit", "m", 19)
print(pers_1.full_name())
pers_1.birthday()
print(pers_1.full_name())
print(pers_1.det_age())


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
class Employee(Person):
    def __init__(self, name, lastname, sex, age, pers_id):
        super().__init__(name, lastname, sex, age)
        if len(str(pers_id)) != 6:
            raise ValueError('Некорректный ввод !')
        self.pers_id = pers_id
        self.level = pers_id % 7

    def __str__(self):
        return super().__str__() + f', ID: {self.pers_id}, level: {self.level}'

    def full_name(self):
        return super().full_name() + f', ID: {self.pers_id}, level: {self.level}'


emp_1 = Employee('Alex', 'Brain', 'm', 23, 123000)
print(emp_1.full_name())
print(f'уровень доступа = {emp_1.level}')
print(emp_1)


# Создайте три (или более) отдельных классов животных.
# Например, рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    def __init__(self, name, age, voice='growl'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    @staticmethod
    def swim():
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    @staticmethod
    def bark():
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    @staticmethod
    def fly_around_corpse():
        print('ooh, meat....')


fish = Fish('Nemo', 2, 'silver', 'bul-bul')
dog = Dog('Spark', 5, 'pit-bull', 'bark!')
bird = Raven('Quasiquotes', 6, 'white', 'bravo!')

animals = [fish, dog, bird]

for i in animals:
    i.make_voice()

fish.swim()
dog.bark()
bird.fly_around_corpse()
