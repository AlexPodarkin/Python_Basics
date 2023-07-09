rows = int(input("Сколько рядов елки"))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

for i in range(1, 10):
    for j in range(2, 6):
        print(f"{j} X {i} = {i * j}", end='\t\t')
    print()
print()
for i in range(1, 10):
    for j in range(6, 10):
        print(f"{j} X {i} = {i * j}", end='\t\t')
    print()

print("решаем квадратное уравнение ax^2+bx+c = 0")
a = float(input("a = "))
print("вы ввели a = ", a)
b = float(input("b = "))
print("вы ввели b = ", b)
c = float(input("c = "))
print("вы ввели c = ", c)

print("решаем квадратное уравнение {}x^2 + {}x + {} = 0".format(a, b, c))
if a == 0:
    if b == 0:
        if c == 0:
            print("уравнений имеет бесконечное число корней")
        else:
            print("ошибка записи уравнения")
    else:
        print("уравнение линейного вида {}x+{} = 0".format(b, c))
        x1 = -c / b
        print("у уравнения только один корень x1= ", x1)
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("у уравнения нет вещественных корней")
    elif discriminant == 0:
        x1 = -b / (2 * a)
        print("у уравнения только один корень x1= ", x1)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print("первый корень уравнения x1= ", x1)
        print("второй корень уравнения x2= ", x2)


while True:
    num = int(input('Введите число от 1 до 999 : '))
    if num < 1 or num > 999:
        continue
    if 10 > num > 0:
        result = f"Введена одна цифра, ее квадрат = {num ** 2}"
    elif 9 < num < 100:
        result = f"Введено двузначное число, произведение цифр = {(num // 10) * (num % 10)}"
    else:
        result = f"Введено трехзначное число, отзеркаленное: {int(str(num)[::-1])}"
    print(result)
    break
