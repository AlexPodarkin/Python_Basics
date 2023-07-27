print("Запись методом write")
text = "Флаг 'a' открываем существующий файл для записи в конец, добавления данных. Если файл \
не существует, создаём новый файл и записываем в него"
with open("data3.txt", "a", encoding="utf-8") as file:
    res = file.write(text + "\n")
    print(f"{res = }\n{len(text) = }")

print("\nЗапись методом write + for")
text2 = ["'W' создаём новый пустой файл для записи.",
         "Если файл существует", " открываем его для",
         " записи и удаляем данные, которые в нём",
         " хранились"]
with open("data3.txt", "w", encoding="utf-8") as file2:
    for line in text2:
        res = file2.write(line + "\n")
        print(f"{res = }\n{len(line) = }")

print("\nЗапись методом writelines")
text3 = ["x — создаём новый пустой ",
         " файл для записи. Если ",
         "файл существует, вызываем ",
         " ошибку."]
with open("data3.txt", "a", encoding="utf-8") as file3:
    file3.writelines("\n".join(text3))

print("\nЗапись print в файл")
text4 = ["Функция 'print' по умолчанию выводит информацию в поток вывода. ",
         " Обычно это консоль. Но можно явно передать файловый объект ",
         "для печати в файл. Для этого надо воспользоваться ",
         " ключевым параметром file."]
with open("data3.txt", "a", encoding="utf-8") as file4:
    file4.write("\n")
    for line in text4:
        print(line, end="***\n## ", file=file4)
