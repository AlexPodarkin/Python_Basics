# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно с кодировкой Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки

# def func_1(text):
#     text.sort()
#     list_1 = []
#     max_x = max([len(i) for i in text])
#     for n, s in enumerate(text, 1):
#         list_1.append(f"{n} {s:->{max_x}}")
#     return list_1
#
#
# text_1 = input("введите строку: ").split()
# print(" \n".join(func_1(text_1)))


# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию
def to_order(string):
    return sorted(set(map(ord, list(string))), reverse=True)


print(to_order("hello python hello"))


# ✔️Функция получает на вход строку из двух чисел через пробел.
# ✔️Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
# ✔️Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def make_dict(str_input: str):
    beg, end = sorted(str_input.split())
    # dict = {ord(x): x for x in range(int(beg), int(end))}
    return {ord(str(x)): x for x in range(int(beg), int(end) + 1)}


print(make_dict('7 3'))
print(ord("3"))
print(chr(51))


# ✔️Функция получает на вход список чисел.
# ✔️Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔️Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


def bubble_sort(sorted_list, str_size):
    for i in range(str_size):
        for j in range(str_size - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]


my_list = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 0, -1]
bubble_sort(my_list, len(my_list))
print(my_list)


# ✔️Функция принимает на вход три списка одинаковой длины:
# ✔️имена str, ✔️ставка int, ✔️премия str с указанием процентов вида «10.25%».
# ✔️Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔️Сумма рассчитывается как ставка умноженная на процент премии.


def treat(list_a, list_b, list_c):
    res_dict = {}
    for i in range(len(list_a)):
        res_dict[list_a[i]] = list_b[i] * float(list_c[i][:-1]) / 100
    return res_dict


print(treat(["i", "p", "s"], [100, 1000, 10_000], ["50%", "25%", "10.25%"]))


# ✔️Функция получает на вход список чисел и два индекса.
# ✔️Вернуть сумму чисел между переданными индексами.
# ✔️Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.


def cut_cum(list_num, start, stop):
    return sum(list_num[min(start, stop) + 1:max(start, stop)])


lst = [i for i in range(100)]

print(cut_cum(lst, 95, 105))


# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
def is_all_rentable(companies):
    return all([sum(i) > 0 for i in companies.values()])


print("res -> ", is_all_rentable({'co1': (1, 5), "co2": (-2, 5)}))

# ✔️Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔️Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
#    на s (кроме переменной из одной буквы s) на None.
# ✔️Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

numbers = [1, 2, 3]
s = 'super'
letter = 'a'


def rename():
    variables = globals()
    temp = {}
    for key, value in variables.items():
        if len(key) > 1 and key.endswith('s'):
            temp[key[:-1]] = variables[key]
            temp[key] = None
    variables.update(temp)


rename()

# короткое решение:
print({key: values for key, values in locals().items() if not key.startswith('__')})
