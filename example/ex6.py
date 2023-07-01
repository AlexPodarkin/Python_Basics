s = "python"
print(type(s))
print(s.upper())
print(s.lower())
print(s.islower())

msg = "abracadabra"
print(msg.count("bra"))
# 2raza
print(msg.count("bra", 4))
# ищем вхождение с 4-го индекса
print(msg.find("cad", 2))

msg2 = msg.replace("a", "o")
# меняет все "а" на "о"
print(msg2)
msg2 = msg2.replace("ob", "OB")
# меняет ob маленькие на большие
print(msg2)
msg2 = msg2.replace("OB", "")
# удалил
print(msg2)

print(msg2.isalpha())
print(msg2.isdigit())

msg = "hi"
print(msg.rjust(10))
# метод используют для заполнения нулями
print(msg.rjust(10, "0"))
#  есть ljust() добавляет нули слева

fio = "Ivanov Ivan Ivanovich"
print(fio.split(" "))
# получили список состоящий из этих строк

digs = "1, 2  ,3, 4   ,5     ,6 ,    7"
digs = digs.replace(" ", "").split(",")
# split создает список из строк
print(digs)

print(", ".join(digs))
# обратная операция соединяет список в строку

print(", ".join(fio.split()))

str1 = " \n  hello \n  world   \n"
print(str1.strip())
# удаляет пробелы и переносы строк !! только в начале и конце !!
# еще есть lstrip & rstrip
