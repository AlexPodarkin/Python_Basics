list_1 = list()
list_2 = []
list_3 = [3.14, True, "Hello_Alex"]

print(list_3[2])
print(list_3[::-1])
print(list_3[-1])

text = "Hello_World"
list_2.extend(text)
print(list_2)
print("метод extend() итерируется по строке и добавляет каждую букву в отдельную ячейку(элемент)!")
list_2.extend(list_3)
print(list_2)
print(list_2.pop(5))
print("удалить по индексу или последний(если мы не укажем аргумент !), и вернет удаленный элемент")
print(list_2)
list_2.remove(3.14)
print("удалить по значению")
print(list_2)
print(list_2.count("l"))
print("кол-во вхождений")
print(list_2.index("l"))
# Индекс ! первого вхождения
list_3.insert(2, "Hello")
print("insert() вставить значение в нужный индекс")
print(list_3)
list_3.insert(-2, "Python")
print("таким образом можно вставлять в конец списка")
print(list_3)

list_4 = [5, 2, 8, 9, 4, 1, 3, 6, 7, 1, 2]
print(list_4)
list_4_sorted = sorted(list_4, reverse=True)
print("сортировка (использовали reverse=True) при помощи ФУНКЦИИ sorted()")
print(list_4_sorted)
list_4.sort()
print("отсортировали основной массив используя МЕТОД .sort()")
print(list_4)
list_4.reverse()
print("реверс имеющегося массива, используя МЕТОД")
print(list_4)
print("реверс имеющегося массива, используя ФУНКЦИЮ, оборачивая и list")
print(list(reversed(list_4)))
print("реверс используя срезы, обрати внимание функция выше не изменила список,\
 а лиш вывела на экран в обратном порядке!")
print(list_4[::-1])
