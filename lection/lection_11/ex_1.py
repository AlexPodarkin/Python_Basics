class User:
    def __init__(self, name, equipment=None):
        self.equipment = [] if equipment is None else equipment
        self.name = name

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'New class {cls}')
        return instance

    def __str__(self):
        return f'Name: {self.name}, List: {self.equipment}'


user_1 = User('Alex')
print(user_1)
user_2 = User('Bob', ['one', 'two'])
print(user_2)
user_3 = User(equipment=['1', '2'], name='Bill')
print(user_3)


print('Ниже SuperInt: метод __new__ для расширения базовых классов')


class SuperInt(int):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args)
        instance.s = "text"
        return instance


num = SuperInt(10)
print(num.s)
print(f'Обратите внимание, что наш класс унаследовал всё, что умеет класс int. Мы смогли сложить '
      f'два числа и получить обычное целое число без свойства name. {num}, их можно складывать {num + 5}')
print('Обрати внимание на тип: ', type(num))
print('Обрати внимание на тип: ', type(num+5))


print('класс Singleton(одиночка):')


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


ex_1 = Singleton('Bob')
ex_2 = Singleton('Alex')
print('создали 2-а экземпляра, получили один ')
print(ex_1.name, ex_2.name)
# таким образом мы можем создать только один экземпляр класса
