# Задача 1
list_1 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 8, 9, 10, 10]
print(list(set(list_1)))

list_2 = []
for i in range(len(list_1)):
    if list_1[i] in list_2:
        continue
    else:
        list_2.append(list_1[i])
print(list_2)

# Задача 2
input_u = input("Введите что хотите -> ")

flag = False
for i in input_u:
    if i.isupper():
        flag = True

if input_u.isdigit():
    print(" Целое = ", int(input_u))
elif flag:
    print(" Есть заглавная, \n  делаем в нижнем регистре: ", input_u.lower())
elif input_u.islower():
    print("Строка в нижнем регистре: ", input_u.lower())
elif isinstance(float(input_u), float):
    print(" Вещественное = ", float(input_u))

tuple_1 = (1, True, 4, False, (1, 2), "Hello", "Alex")
print(tuple_1)

dict_1 = {}
print(dict_1)

for i in tuple_1:
    dict_1[i] = [i] * 3
print(dict_1)
