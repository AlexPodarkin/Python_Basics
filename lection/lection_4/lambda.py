# lambda анонимные функции
my_dict = {"two": 2, "three": 3, "one": 1}
print(my_dict)
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(s_value)

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
print(my_list)
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

current_list = [1, 2, 3, 4, 6, 10, 11, 15, 12, 14]
print("Пример с map()")
new_list = list(map(lambda x: x * 2, current_list))
print(new_list)
