text = "Hello Alex"
print(text.find("l"))
print(text.find("z"))
# Находит индекс первого вхождения аналогично методу (.index), если не находит вернет -test а index вернет ошибку
num = 321321654463123
print(f"{num = :_}")
list_1 = [213211, 654654654, 987, 98789, 2525, 7, 8798, 79889, 2525, 789798]
for i in list_1:
    print(f"значение {i :>12}")
# классный способ делать все ровно !

# a, b, c, *_ = map(int, input("Введите не менее 3-х чисел: ").split())
# print(a, b, c)

print(" - ".join(["i", "learning", "python"]))
# .join метод склеивает список строк(через нужный разделитель), числа у меня не сработали
print("python".upper())
print("i learning python".title())
# с большой буквы
print("i learning python".startswith("i"))
# возвращает True если строка начинается с заданного символа или слова
print("i learning python".endswith("python"))
# возвращает True если строка заканчивается заданным символом или слова
