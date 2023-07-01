# срезы

list1 = ["Moscow", "Ufa", "Kazan", "Astrakhan"]

print(list1[1:3])

city = list1
print(id(list1))
print(id(city))
# одинаковы ! это ссылка
print("\n")

city2 = list1[:]
# с помощью среза создается копия списка
print(id(city))
print(id(city2))
# id разные это копия! (так можно копировать списки)
# или
city3 = list(city2)
print(id(city3))
# все 3 списка копии

s1 = "king,kja k jk j kk j jlk, ds,"
s1 = s1.replace(" ", "").replace(",", "")
s1 = s1[1:14]
print(s1)
print(s1.split("k"))

list1 = ["Moscow", "Ufa", "Kazan", "Astrakhan"]
print(list1)
list1[1:3] = ["Kazan", "Ufa"]
print(list1)

list1 += ["Volgograd"]
print(list1)

list1[0:2] = [10, 20]
print(list1)

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] > [1, 2, 3])
print([1, 2, 3] != [1, 2, 3])
# внимание ! проверяет по элементам как список
# не проверяет все, останавливается на элементе, где есть разница
print([1, 100, 100] < [10, 2, 3])
# вернет True потому что 0 элемент первого меньше !
