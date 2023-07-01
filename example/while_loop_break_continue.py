list1 = [1, 5, 5, 9, 7]
flag = False
i = 0
while i < len(list1):
    if list1[i] % 2 == 0:
        flag = True
        break
    i += 1

if flag:
    print("четное есть")
else:
    print("четного нет")


while i < len(list1) and list1[i] % 2 != 0:
    print(i)
    i += 1

s = 0
d = 1
while d != 0:
    d = int(input("Введите число -> "))
    if d % 2 == 0:
        continue

    s += d
    print("s = " + str(s))

a = 1
res = 1
b = 1

while b != 0:
    res = res + (a / b)
    b = int(input("введите число -> "))
else:
    print("на ноль делить нельзя !")
print("ответ -> ", res)

S = 0
i = -5

while i < 100:
    if i == 0:
        break
    S += 1/i
    i += 1
else:
    print("сумма вычислена корректно")
print("ответ -> ", S)
