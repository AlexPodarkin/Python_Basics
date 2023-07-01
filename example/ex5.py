text = '''Hello my friends'''
print(text + "\n")
print(text[0])
print(text[0:5], text[:5])
print(text[-1], text[len(text) - 1])
# это равнозначные записи
print(text[5:])
print("Panda"[0])
print(text[::3])
# start : stop : step
print(text[2:-2])
print(text[::-1])
# reverse

text2 = "h" + text[1:]
print(text2)
# исправили букву, получили новую строку
# строки неизменяемый тип данных
