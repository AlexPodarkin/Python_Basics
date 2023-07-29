a, b, c, *d = "test/2/3/4/5/6/7/8/9".split("/")
print(a, b, c, d)
my_dict = dict()
my_dict[b] = a
my_dict[c] = ", ".join(d)
print(my_dict)

text = "Hello_Python"
my_dict2 = {i: ord(i) for i in text}
print(my_dict2)

my_iter = iter(my_dict2.items())
print(*(next(my_iter) for _ in range(5)))

# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.
print(*(i for i in range(0, 101, 2) if sum([int(j) for j in str(i)]) != 8))


# ✔Напишите программу, которая выводит на экран числа от test до 100.
# ✔При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔Вместо чисел, кратных пяти — слово «Buzz». ✔Если число кратно и 3, и 5,
# то программа должна выводить слово «FizzBuzz». ✔*Превратите решение в генераторное выражение.
print(*('FizzBuzz' if not i % 15
        else "Buzz" if not i % 5
        else "Fizz" if not i % 3
        else i
        for i in range(1, 101)))

# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


def simple_nums(n):
    res_2 = iter([i for i in range(2, n * 10) if all(i % j != 0 for j in range(2, i))])
    for i in range(n):
        yield next(res_2)


iter_simple_nums = iter(simple_nums(5))
print(next(iter_simple_nums))
print(next(iter_simple_nums))
print(next(iter_simple_nums))
