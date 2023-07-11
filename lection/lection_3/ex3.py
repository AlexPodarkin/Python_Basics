print("Картежи")
turtle_1 = tuple(range(3))
print(turtle_1)
turtle_2 = ()
turtle_3 = (1, 2, 3)
print(turtle_3)
# картежи не изменяемый тип данных
# метод count() index() len() работают с картежами
print("Третий элемент кортежа =  ", turtle_3[2])
# срезы и обращения поэлементно тоже работают


print("Словари")
a = {"one": 42, "two": 3.14, "ten": "Hello"}
b = dict(one=42, two=3.14, ten="Hello")
c = dict([["one", 42], ("two", 3.14), ("ten", "Hello")])
# списки и кортежи по 2-а элемента можно преобразовать в словарь
print(a == b == c)
my_dict = a.copy()
print(my_dict)

my_dict["ten"] = 10
# добавление элемента
print(my_dict)
print(my_dict["two"])
print(my_dict.get("one"))
print(my_dict.get("one", "Значение по default , может быть int и пр."))
# получение значения по ключу
# если значения нет то выдаст ошибку, а метод get вернет None или значение после запятой(только в случае если не найдет)
print(my_dict.setdefault("five"))
print(my_dict)
print(my_dict.setdefault("six", 6))
print(my_dict)
print(my_dict.setdefault("two", 6))
# изменения "my_dict.setdefault" происходят только тогда когда значение в словаре отсутствует
print(my_dict)

print(my_dict.keys())
# так используют редко (выводит список ключей)
for key in my_dict.keys():
    print(key, end=" | ")

print()
# метод ".keys()" позволяет обратиться к ключам в словаре
for value in my_dict.values():
    print(value, end=" | ")
print()
# метод ".values()" позволяет обратиться к значениям в словаре

for key, values in my_dict.items():
    print(key, values)
# метод ".items()" выводит пару ключ значение

print("'popitem()' удалил последнее значение и вернул =  ", my_dict.popitem(), "словарь теперь выглядит так: ", my_dict)
print("'pop()' удалил значение в скобках и вернул =  ", my_dict.pop("one"), ", словарь теперь выглядит так: ", my_dict)

print(" метод '.update' добавляет значения в словарь, вернул ", my_dict.update({"ten": 10, "Hello": 5}), my_dict)
# если ключ был, то значение обновится, а ключ останется на своем месте !

new_dict = my_dict | {"ten": 10, "Hello": 7} | dict(six=6)
# такая запись актуальна с версии 3.10
