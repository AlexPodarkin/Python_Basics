s = "Hello\n\t \"Wrld"
# \ этим символом можно экранировать кавычки и прочие символы
print(len(s))
print(s)

path = "D:\Python\text.txt"
print(path)
# Экранировать пути обязательно во избежание ошибок !!!
path = "D:\\Python\\text.txt"
# только так !
print(path)

path = r"D:\Python\text.txt"
print(path)
# еще один вариант это роу строки r""
