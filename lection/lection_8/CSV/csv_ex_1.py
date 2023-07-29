import csv

with open(' biostats.csv', 'r', newline='') as file:
    csv_file = csv.reader(file)
    for line in csv_file:
        print(line)
# Важно! При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.


# Файл biostats_tab.csv хранит те же данные, что и файл выше, но вместо разделителя
# используется символ табуляции. По сути это разновидность TSV — файл с
# разделителем табуляцией.
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab',
                          quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))
# ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
# ➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу,
# указывающую функции, что числа без кавычек необходимо преобразовать к типу float.

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        all_data.append(line)
    csv_write.writerows(all_data)

print("Чтение в словарь -> ")
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"], restkey="new",
                              restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')
