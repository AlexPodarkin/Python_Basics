import math
import decimal
import fractions

# text.txt = input("введите текст: ")
#
# if text.txt.isdigit():
#     bin_num = bin(int(text.txt))
#     oct_num = oct(int(text.txt))
#     hex_num = hex(int(text.txt))
#     print("двоичная = ", bin_num, "восьмеричная = ", oct_num, "шестнадцатеричная = ", hex_num)
# elif text.txt.isascii():
#     print("Текст написан согласно таблице ASCII")
# else:
#     print("Текст написан НЕ согласно таблице ASCII")

# работа с библиотекой math,  decimal, fractions
print(math.pi, math.e, math.inf, math.nan, math.tau, sep=" | ")

pi = 3.141592653589793123321123321123
print(pi)
pi = decimal.Decimal("3.141592653589793123321123321123")
print(pi)
# для точных расчетов используй библиотеку decimal

# модуль fractions для работы с дробями
f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f1 * f2)

print(abs(-5))
# по модулю
print(divmod(14, 4))
# разделить и вывести целое + остаток (в кортеже)
print(pow(2, 3))
# возвести в степень
print(round(0.33500021212, 2))
# округлить (правила округления как в школе)
