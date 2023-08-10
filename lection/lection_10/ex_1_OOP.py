class PersonGame:
    def __init__(self, name, damage, health):
        self.__name = name
        self._damage = damage
        self._health = health

    def attack(self, other_pers):
        other_pers._health -= self._damage
        self._health += self._damage * 0.5

    def __str__(self):
        return f'Name: {self.__name}, damage: {self._damage}, health: {self._health}'


class HeroOne(PersonGame):
    def __init__(self, name, damage, health, baf):
        super().__init__(name, damage, health)
        self.baf = baf

    #     переопределение методов
    def attack(self, other: PersonGame):
        other._health -= self._damage * self.baf
        self._health += self._damage * self.baf

    def __str__(self):
        return super().__str__() + f', baf: {self.baf}'


pers_1 = PersonGame('Kir', 10, 100)
pers_2 = PersonGame('Sam', 10, 100)
print(type(pers_1))
print(pers_2)
pers_1.attack(pers_2)
pers_1.attack(pers_2)
print(pers_1)
print(pers_2)
hero_1 = HeroOne('Serafim', 10, 100, 2)
# полиморфизм: Один и тот же метод '.attack' по-разному применяет параметр health у обычного персонажа и у героя.
print(hero_1)
hero_1.attack(pers_1)
print(hero_1)
print(pers_1)


class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'


class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'


class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None, country=None,
                 city=None, street=None, left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._max_level * 2)


p1 = Hero('archery', 'Сильвана', 'Эльф', 120, country='Эльфляндия', street='Ночного эльфа', left_hand='Стрела')
print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')
