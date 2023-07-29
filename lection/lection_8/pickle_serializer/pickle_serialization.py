# Крайне важно! Модуль pickle не занимается проверкой потока всех байт на безопасность перед распаковкой.
# Не используйте его с тем набором байт, безопасность которого не можете гарантировать !!!!
import pickle

data = pickle.loads(b"cos\nsystem\n(S'echo I hacked you!'\ntR.")
print(f"Вот что тебе вернули -> {data = }. То что ты увидел в консоли ! Это результат работы функции .loads выше !\n")

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children":
        [
            {
                "first_name": "Алиса",
                "age": 5
            },
            {
                "first_name": "Маруся",
                "age": 3
            }
        ]
}

print("Сериализаця")
data = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print("Отдельно указали протокол по умолчанию. Модуль pickle имеет несколько протоколов,"
      " который не гарантируют совместимость с более старыми версиями.")
print(f'{data = }')


def func(a, b, c):
    return a + b + c


my_dict = \
    {
        "numbers": [42, 4.1415, 7 + 3j],
        "functions": (func, sum, max),
        "others": {True, False, 'Hello world!'},
    }
with open('my_dict.pickle', 'wb') as file:
    pickle.dump(my_dict, file)
print("Функция dump принимает на вход объект для сериализации и файловый дескриптор")

print("\nДесериализация")
new_dict = pickle.loads(data)
print(f"{new_dict = }")

print("\nВ финале загрузим данные из файла my_dict.pickle")
with open('my_dict.pickle', 'rb') as file_2:
    new_dict = pickle.load(file_2)
print(f'{new_dict = }')
print(f'{new_dict["functions"][2](2, 10, 4) = }')
print(" Внимание, В файле, где произведена десериализация есть функция func, которая складывает числа. "
      "Модуль pickle указал в словаре её, а не исходную. Более того, если бы функции с нужным именем не было, "
      "десериализация завершилась бы ошибкой.(т.е файл сериализации и десериализации должны быть идентичны ! )")
