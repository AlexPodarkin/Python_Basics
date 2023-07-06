# квадратичная последовательность
n = 6
array = [1] * n

for i in range(n):
    array[i] = i ** 2
print(array)

# с помощью list comprehensions кубическая последовательность
array = [x ** 3 for x in range(n)]
print(array)

array2 = [1 for x in range(5)]
print(array2)

array3 = " <*> ".join([str(k) for k in array2])
print(array3)
# c помощью list comprehensions можно преобразовывать списки !

array4 = [x % 4 for x in array]
print(array4)

array5 = [x % 2 == 0 for x in array]
print(array5)

array5 = [x * 0.5 + 1 for x in array]
print(array5)

num = input("Введите числа через пробел: ")
array6 = [int(x) for x in num.split()]
print(array6)

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(numbers)

print([x for x in array if x % 2 != 0])

cities = ["Moscow", "Ufa", "Yar", "Kirov"]
cities2 = [c for c in cities if len(c) < 4]
# в list comprehensions можно добавлять условие
print(cities2)

num = [1, 2, 3, 4, 5, 5, 5, 7, 7, 7]
num_type = ["нечетное" if x % 2 != 0 else "четное" for x in num]
# так-же в list comprehensions можно использовать тернарный оператор
print(num_type)

num_type = ["нечетное" if x % 2 != 0 else "четное" for x in num if x % 5 != 0]
# так-же в list comprehensions можно использовать тернарный оператор + условие в конце
print(num_type)
