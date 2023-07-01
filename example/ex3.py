a = -6.84
b = 7
print(abs(a))

c = "Hello"

print(a, b, c, sep=" | ")

print("Hello", end=" ")
print("World !")
print("Координаты: х = ", a, "; у = ", b, sep="")

print(f"Координаты: х = {a}; у = {b}")

d = input("Введите: ")
print("Вы ввели: " + d, "тип: ", type(d))
# все строка !!! что мы ввели в консоли !

e = abs(int(d))
# не забывай приводить данные к числу !
print(e)

f = float(input("Введите: "))

print("Периметр = ", (e + f) * 2)

g, h = map(float, input("Введите 2 цифры через пробел: ").split())
print("Периметр = ", (g + h) * 2)
