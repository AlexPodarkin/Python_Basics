num = "1111"
num = int(num, base=2)
print(num)
print(2 ** 16 - 1)
bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)
print("двоичная = ", bin_num, "восьмеричная = ", oct_num, "шестнадцатеричная = ", hex_num)
# обрати внимание на вывод ! первые 2-а символа обозначают систему счисления !

list_el = [15, 15, 5.5, "Hello", True]
for i in range(len(list_el)):
    print(i + 1, end=" | ")
    print("Значение -> ",list_el[i], end=" | ")
    print("Адрес в оперативной памяти ", id(list_el[i]), end=" | ")
    print("Размер", list_el[i].__sizeof__(), end=" | ")
    print("hash = ",hash(list_el[i]), end=" | ")
    print("является числом" if isinstance(list_el[i], int) else "не является целым числом", end=" | ")
    print("является строкой" if isinstance(list_el[i], str) else "не является строкой")
    print("-" * 150)
# обрати внимание, что в памяти число 15 имеет одинаковый адрес (ссылочный тип данных)
# ссылаются на один и тот-же объект


select_s = int(input("Введите систему счисления (2 - 8)-> "))
res = ""
n = int(input("Введите число: "))
n1 = n
while n > 0:
    res = str(n % select_s) + res
    n = n // select_s
print(f"Ваше число в {select_s}-ной системе счисления = ", res)
# проверка
print(bin(n1)[2:] if select_s == 2 else (oct(n1)[2:] if select_s == 8 else "вы не выбрали 2 или 8"))


total_cash = 0
count = 0
while True:

    if total_cash > 5_000_000:
        total_cash *= 0.9

    print("сумма на счете ", total_cash)

    print("test - пополнить")
    print("2 - снять")
    print("0 - выйти")

    action = input("введите номер операции: ")

    match action:
        case "test":
            add = int(input("внесите сумму кратную 50: "))
            if add % 50 == 0:
                total_cash += add
                count += 1
            else:
                print("неверная сумма")
        case "2":
            take = int(input("введите сумму снятия кратную 50: "))
            if take % 50 == 0:
                percent = take * 1.5 * 0.01
                if percent < 30:
                    percent = 30
                if percent > 600:
                    percent = 600

                if total_cash < (take + percent):
                    print("недостаточно средств")
                else:
                    total_cash -= (take + percent)
                    count += 1
            else:
                print("неверная сумма")
        case "0":
            quit()

    if count == 3:
        total_cash *= 1.03
        count = 0
