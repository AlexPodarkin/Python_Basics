dictionary = {"house": "дом", "car": "машина", "tree": "дерево", "road": "дорога"}

print(dictionary)

# получение значения по ключу
print(dictionary["car"])

# так-же словарь можно создать функцией dict()
dictionary2 = dict(one=1, two=2, tree=3)

list_grades: list[list[int | str]] = [[2, "неуд"], [3, "удв"], [4, "хор"]]
# с помощью функции dict() можно преобразовать 2-х мерный список в массив
# noinspection PyTypeChecker
dictionary3 = dict(list_grades)
print(dictionary3)

dictionary4 = dict()
dictionary4[True] = "Истина"
dictionary4[False] = "Ложь"
print(dictionary4)
dictionary4[3] = "Три"
print(dictionary4)
dictionary4[3] = "Tree"
print(dictionary4)
# ключом могут быть только неизменяемые типы данных (список не может быть ключом например)
# в качестве значения можно использовать любые типы данных
print(len(dictionary4))

# удалить значение можно с помощью функции del
del dictionary4[True]
print(dictionary4)

# как проверить есть ли ключ?
print(False in dictionary4)
print(3 in dictionary4)
print(not "2" in dictionary4)
# эта проверка относится к ключу !!
