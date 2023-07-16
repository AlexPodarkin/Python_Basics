# Функция chr(integer)
# Функция возвращает строковой символ из таблицы Юникод по его номеру. Номер -
# целое число от 0 до 1_114_111.
print(chr(98))
print(chr(1073))
print(chr(128519))

# Функция ord(char)
# Функция принимает один символ и возвращает его код в таблице Юникод.
print(ord('b'))
print(ord('б'))
print(ord('😉'))

SIZE = 10

print(locals()) 
print(globals())
print("---" * 50)
print("только глобальные(сортировка без DUNDER__ методов ): ", end="")
print(*filter(lambda x: not x[0].startswith("__"), globals().items()))
