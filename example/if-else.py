x = -5
if x < 0:
    x = abs(x)
else:
    print("число положительное :) = ", end="")
print(x)

a = float(input("введите 1е число: "))
b = float(input("введите 2е число: "))

if a > b:
    print("1е больше второго")
elif a == b:
    print("числа равны")
else:
    print("2е больше первого")

c = float(input("введите число: "))
if 0 <= c <= 10:
    print("число в диапазоне от 0 до 10")

marks = [3, 4, 5, 3, 5]
if 2 in marks:
    print("студент будет отчислен !")
else:
    print("студент успешно сдал сессию")

d = float(input("введите число: "))
if d % 2 == 0:
    print("число четное")
else:
    print("число не четное")
