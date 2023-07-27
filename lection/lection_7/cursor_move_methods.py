# Методы перемещения в файле
print("\nМетод tell")
text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
        'Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())

print("\nМетод seek")
last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))

print("\nМетод truncate")
last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())

with open('new_data.txt', 'r+', encoding='utf-8') as data:
    data.seek(0, 2)
    data.write("data.seek(0, 2) переводит курсор в конец файла ")
    data.write("'r+' - позволяет открыть файл на чтение и запись ")
