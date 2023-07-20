data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print("этот принт не сработал ! -> ", *list_iter)
#  Обратите внимание, что итератор является одноразовым
# объектом. Получив все элементы коллекции один раз он перестаёт работать.
# Для повторного извлечения элементов необходимо создать новый итератор.

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

# Перед вами несколько строк кода
# Напишите, что выведет каждая из строк, не запуская код
data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x)
y = next(x)
print(y)
z = next(iter(y))
print(z)
