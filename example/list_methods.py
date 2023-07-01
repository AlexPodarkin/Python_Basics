list1 = [1, 2, 3, -55, 100, -7, 4, 5, 6]
print(list1)
list1.append(100)
print(list1)

list1.insert(3, -1000)
print(list1)

list1.remove(-1000)
# удаляет конкретный элемент (который мы указали в скобках)
print(list1)
# если происходит удаление не существующего значения, компилятор выдаст ошибку

del_el_list1 = list1.pop()
# удаляет и возвращает последнее значение
print(list1)
print(del_el_list1)
# также с ее помощью можно удалить элемент по индексу
list1.pop(0)
print(list1)

list1.clear()
print(list1)

list1 = [1, 2, 3, -55, 100, -7, 4, 5, 1]

list2 = list1.copy()
print(list2)

print(id(list1))
print(id(list2))
# это копия ! не ссылка

print(list1.count(1))
# сколько единиц в списке

print(list1.index(3))
# возвращает индекс найденного значения

print(list1.index(1, 7))
# можно указать с какого элемента начать поиск
print(1 in list1)

print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list1 = ["Moscow", "Ufa", "Kazan", "Astrakhan"]
list1.sort()
print(list1)
# строки тоже сортируются

line = [1, 6, 11, 3, 7]

img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]

print(img)

print(img[1])
print(img[0][1])

img[0] = [0, 0, 0, 0, 0]
print(img)

img[1] = [0] * 5
print(img)
# тут поменяли ссылку

img[2][:] = [1] * 5
print(img)
# в данном случае поменяли значения
