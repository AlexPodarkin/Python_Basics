a = -10
b = -15

res = a if a > b else b
print("максимальное = ", res)
# в тернарных операциях можно пользоваться функциями
res = abs(a) if a > b else abs(b)
print("максимальное = ", res)

s = 'python'
t = 'upper'
res = s.upper() if t == 'upper' else s
print(res)

print([1, 2, a if a > b else b, 3, 4])
# тернарный оператор как некий активный объект

print("numbers 'a' - " + ("нечетное" if a % 2 != 0 else "четное ") + "число")
# пример со строками

print([1, 2, a if a > b else b])
# пример со списком

a = 9
b = 8
c = 17
# большее из 3-х чисел с использованием тернарного оператора
print((a if a > c else c) if a > b else (b if b > c else c))
# такие конструкции обычно не используют
