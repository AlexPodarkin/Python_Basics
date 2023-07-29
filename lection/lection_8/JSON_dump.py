import json

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
print("функция сериализации dump ->")
print(f'У нас словарь, мы запишем его в файл "new_user.json" -> {type(my_dict)}\n')
with open('new_user.json', 'w') as file_2:
    json.dump(my_dict, file_2, ensure_ascii=False)
# Json.dump принимает то что нужно сохранить + файл(файловый дескриптор) куда сохранить(файл должен быть открыт)
# дополнительный параметр для кириллицы ensure_ascii.
# Ensure_ascii=False (если мы хотим отказаться от символов экранирования в JSON файле)

print("функции десериализации файла .load и получение значения ->")
with open("new_user.json", "r") as file:
    my_dict2 = json.load(file)

print(f"получил данные -> {my_dict2['children'][0]['first_name']}")
print('результат -> тот-же словарь, произвели сериализацию и десериализацию файла')

print("\nВоспользуемся словарём my_dict ещё раз для проверки функции dumps !")
dict_to_json_text = json.dumps(my_dict)
print(f'тип после -> {type(dict_to_json_text)}')
print(f'результат -> {dict_to_json_text }')

print("Дополнительные параметры dump и dumps -> ")
dict_to_json_text_2 = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(dict_to_json_text_2)
# ➢ Параметр indent отвечает за форматирование с отступами. Теперь JSON
# выводится не в одну строку, а в несколько. Читать стало удобнее, но размер увеличился.
# ➢ Параметр separators принимает на вход кортеж из двух строковых элементов.
# Первый — символ разделитель элементов. Второй — разделитель ключа и значения.
# ➢ Параметр sort_keys отвечает за сортировку ключей по алфавиту

print("\nВоспользуемся результатом res для проверки функции loads (функции десериализации строки)!")
text_json_to_dict = json.loads(dict_to_json_text_2)
print(f'тип после -> {type(text_json_to_dict)}')
print(f'результат -> {text_json_to_dict}')
print(f'результат -> тот-же словарь только отсортированный, произвели сериализацию и десериализацию строки')
