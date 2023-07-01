print("List")
#  ctr + alt + l это авто форматирование кода в этом редакторе
list1 = ["Moscow", "Kazan", "Astrakhan"]

marks = [2, 3, 4, 7, 4, 5]

print(marks[0])
print(marks[-1])

print(sum(marks) / len(marks))

marks[0] = 10
print(marks)
# списки в отличие от строк изменяемый тип данных !
# динамическая структура данных
marks[1] = "удв"
print(marks)

b = list()
a = []
# задать пустой список

print(list("Python"))
# list может формировать новые списки из итерируемых объектов

marks = [100, 3, 4, 7, 4, 5]
print(len(marks))
print(max(marks))
print(sorted(marks))
print(marks)
# обрати внимание он его не отсортировал только, вывел
# ниже другой способ !
marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks, "\n")

s = list("python")
print(s)
print(max(s))
# ACII определяется числовым значением
print(sorted(s))
print(s)

print([1, 2, 3] + [4, 5, 6])
# объединение списков
list2 = ["i", "love", 'python']*3
print(list2)

print("love" in list2)

print(list2[0].isdigit())

del list2[0]
print(list2)
