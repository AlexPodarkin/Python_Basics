print("Hello Alex".__doc__)
print("Hello World".count("l"))
# выше метод нахождения количества вхождений

# справка атрибутов любого объекта
print(dir("object"))
# интерактивная справочная система
print(help(str))

num = "101"
num = int(num, base=2)
print(num)

print(2 ** 16 - 1)
bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)
print("двоичная = ", bin_num, "восьмеричная = ", oct_num, "шестнадцатеричная = ", hex_num)
# обрати внимание на вывод ! первые 2-а символа обозначают систему счисления !

print(0.1 + 0.2)
# из-за особенностей хранения чисел возникает неточность в результате !
