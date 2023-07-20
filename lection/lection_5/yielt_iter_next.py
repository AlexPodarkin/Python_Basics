print("Как вы помните команда return возвращает готовый результат работы функции и\
завершает её работу. Зарезервированное слово yield превращает функцию в\
генератор. Значение после yield возвращается из функции. Сама функция\
запоминает своё состояние: строку, на которой остановилось выполнение, значения\
локальных переменных. Повторный вызов функции продолжает работу с момента остановки.")


def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


# выше функция для расчета факториала
for count, num in enumerate(factorial(10), start=1):
    print(f'{count}! = {num}')
# Функции iter и next для генераторов
# Уже знакомые по сегодняшнему уроку функции iter и next могут работать с
# созданными генераторами. Например, так:
my_iter = iter(factorial(5))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# Задание
# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код.


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }', end=" | ")

my_iter = iter(gen(10, 1))
print("\n Это итератор -> ", my_iter)
print("вызываем значение по порядку и т.д ->", next(my_iter), next(my_iter), next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))