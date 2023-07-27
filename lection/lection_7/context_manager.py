# Менеджер контекста with open
# with гарантирует закрытие файла и сохранение информации

with open("data.txt", 'r+', encoding="UTF-8") as text:
    print(list(text))
    text.write("goodbye\n")
# после этого with гарантирует закрытие файла и сохранение информации

with open("data.txt", 'r+', encoding="UTF-8") as text, open("data2.txt", 'r+', encoding="UTF-8") as text2:
    print(list(text))
    text2.write("второй файл \n")
    print(list(text2))

print("\nПредпочтительный вариант (python 3.10)")
with (
    open('data.txt', 'r+', encoding='utf-8') as f1,
    open('data.txt', 'r+', encoding='utf-8') as f2
):
    print(list(f1))
    print(list(f2))
