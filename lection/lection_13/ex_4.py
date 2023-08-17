class UserException(Exception):
    pass


class UserAgeError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Возраст пользователя должен быть целым int() или вещественным float() больше нуля." \
           f"  У вас тип {type(self.value)}, а значение {self.value}"


class UserNameError(UserException):
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = 'попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.lower:
            text = 'больше верхней'
        return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов). ' \
               f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'


class User:

    MIN_LEN = 6
    MAX_LEN = 15

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
            self.age = age
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)


user = User('Яковлев', '-12')
