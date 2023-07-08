a = "5"
print(a.isdigit())
# этот метод проверяет строку ! является ли она числом
print(isinstance(a, str))
# а эта функция проверяет тип данных !
b = 3.14
print(isinstance(b, (int, float, complex)))
# функция может принимать несколько аргументов в картеже

# пример
num = 6
digit = 6.0
print(num, " & ", digit)
print(num == digit)  # True числа одинаковы
print(num is digit)  # False
# оператор is сравнивает не значения, а объекты по их идентичности int != float

txt = "Hello World"
print(id(txt))
txt = txt.replace(" ", "_")
print(txt)
print(id(txt))
# Это разные объекты ! Потому-что строки неизменяемый тип данных
# Не изменили, мы создали новый объект

# аннотация типов
# в первой переменной указан int или float
c: int | float = 10.0
d: float = 2.0
print(c / d)


def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res


# аннотация типов (пример с функцией)

print(my_func([5, 5, 5, 25]))
