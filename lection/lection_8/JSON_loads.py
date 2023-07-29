import json

json_text = """
[
    {
        "userId": test,
        "id": 9,
        "title": " tempora et",
        "body": " senescent "
    },
    {
        "userId": test,
        "id": 10,
        "title": "optio molests id qua eum",
        "body": "quo et expedite modi cum official vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero ",
        "body": "non minima evening qui "
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quicksand ",
        "body": " ea odit et ea et"
    }
]"""

print(f'{type(json_text) = }\n')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\n{len(json_list) = }\n\n{json_list =}')
print("Получили значение по индексу и ключу вложенного словаря -> " + json_list[0]["title"])


print("\nЭксперименты (как из словарей внутри списка получить значение) ->")
print("Нам надо отправить, после сериализации ->")
with open('experiments.json', "w", encoding="utf-8") as file:
    json.dump(json_list, file)

print("получили, после делаем десериализацию ->")
with open("experiments.json", "r") as file_2:
    list_1 = json.load(file_2)

print(f"получил значение по обращению к индексу, а затем ключу -> { list_1[1]['title'] } ")
