# list(f)
print("->Чтение в список")
with open("data.txt", 'r+', encoding="UTF-8") as text:
    print(list(text))

# res = f.read()
print("\n-> Чтение методом read")
with open("data.txt", 'r+', encoding="UTF-8") as text_2:
    res = text_2.read()
    print(f'Читаем первый раз:\n{res}', end="")
    res = text_2.read()
    print(f'Читаем второй раз (пусто):\n{res}', end="")
#       метод .read(5) может принимать количество считываемых символов


# res = f.readline()
print("\n-> Чтение методом readline, читает строку + \\n")
with open("data.txt", 'r+', encoding="UTF-8") as text_3:
    print(text_3.readline(), end="")
    print(text_3.readline(), end="")


# for line in f:
print("\n-> Чтение циклом for")
with open("data.txt", 'r+', encoding="UTF-8") as text_4:
    for line in text_4:
        print(line, end="")
#       что-бы избавится от переноса можно использовать срезы line[:-1] или метод line.replace("\n","")
