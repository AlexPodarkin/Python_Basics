import json

print("-=Модуль JSON=-")

with open("user.json", 'r', encoding="utf-8") as file:
    json_file = json.load(file)

print(f'{type(json_file) = }\n{json_file = }\n')
print(f'{json_file["name"] = }\n')
print(f'{json_file["address"]["geo"] = }\n')
print(f'{json_file["email"][0] = }')
