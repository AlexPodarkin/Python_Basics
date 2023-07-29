import random

print("\t- Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.\
 Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого \
 отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется \
 больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно\
  сообщить является ли треугольник разносторонним, равнобедренным или равносторонним")
a = float(input("введите test-ую сторону = "))
b = float(input("введите 2-ую сторону = "))
c = float(input("введите 3-ую сторону = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")
else:
    print("Треугольник не существует")

print("\t- Напишите код, который запрашивает число и сообщает является ли оно простым или составным.\
 Используйте правило для проверки: «Число является простым, если делится нацело только на единицу\
  и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.")
n = int(input("Введите число -> "))
flag = True
i = 2

if n < 0:
    print("ограничение на ввод отрицательных чисел !")
elif n > 100_000:
    print("ограничение на ввод чисел больше 100 тысяч !!")
else:
    while i <= n ** 0.5:
        if n % i == 0:
            flag = False
            break
        i += 1
    if flag:
        print("Простое число")
    else:
        print("Составное число")

print("\t- Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна\
 подсказывать «больше» или «меньше» после каждой попытки.Для генерации случайного числа используйте код:\
  from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)")
random_num = random.randint(0, 1_000)
num = None
attempts = 10
while attempts > 0:
    num = int(input(f"Угадай какое число я загадал от 0 до 1000 ? ( количество попыток: {attempts} ) -> "))
    attempts -= 1
    if random_num > num:
        print("я загадал число БОЛЬШЕ твоего !")
    elif random_num < num:
        print("я загадал число МЕНЬШЕ твоего !")
    else:
        print("Мои поздравления!!! ТЫ УГАДАЛ !!!")
        break
else:
    print("Ты не угадал :р , не расстраивайся :)")
print("Хорошего Дня !")
