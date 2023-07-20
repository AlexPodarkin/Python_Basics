print("Что будет, если генераторное выражение записать не в круглых скобках, а в\
квадратных? Получим list comprehensions")
my_list_comp = [chr(i) for i in range(97, 123)]
print(my_list_comp)  # ['a', 'b', 'c', 'd', ..., z]
for char in my_list_comp:
    print(char)

print("простейший пример, вывода четных чисел используя генератор (j for j in range(11)) и list comprehensions")
res = [item for item in (j for j in range(11)) if item % 2 == 0]
print(res)
print("Генераторные выражения или генерация списка\
В примере из раздела “генераторные выражения” мы обернули генератор\
функцией list, чтобы сохранить значения в список. Можно воспринимать это как\
анти пример кода. Какой же пример является верным? Если на выходе нужен\
готовый список, оптимальным будет следующий код:")
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')

res = [i + j for i in x
       if i % 2 != 0
       for j in y
       if j != 1]
print(f'{len(res)=}\n{res}')
print("с первого списка(x) берем нечетные, со второго(y) все кроме единицы")

print("Set comprehensions (меняются только скобки)")
my_set_comp = {chr(i) for i in range(97, 123)}
print(my_set_comp)

print("Dict comprehensions")
my_dict_comp = {i: chr(i) for i in range(97, 123)}

for key, value in my_dict_comp.items():
    print(f"ASCII: {key} number: {value}")
# Важно! Стоит помнить, что ключи словаря должны быть объектами
# неизменяемого типа.
