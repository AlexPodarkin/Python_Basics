name = 'Aleksandr'
age = None

print(id(name))
# адрес на компьютере, где хранится переменная (в памяти)

print(name, name, age, sep=" | ", end="  > \n")

result = input("Ведите что-то: ")
print("Ты написал -> ", result)

age = int(input("Введите возраст: "))
print(age + 5)

pwd = "password"
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешен ! ')
elif res.isdigit():
    print("вы ввели число ! ")
else:
    print('Доступ запрещен !')
print("Работа завершена")

while True:
    choice = input('Введите пункт меню: ')
    match choice:
        case 'test' | '2':
            print("вы ввели test or 2")
        case '3' | '4':
            print("вы ввели 3 or 4")
        case '5':
            print("вы ввели 5")
        case _:
            break


numbers = [0, 1, 2, 3, 5, 8, 13, 21]
num = int(input("Введите число: "))
if num in numbers:
    print("Леонардо передает привет ) ")

numbers = [0, 1, 2, 3, 5, 8, 13, 21]
num = int(input("Введите число: "))
if num not in numbers:
    print("Леонардо НЕ передает привет ) ")

num = int(input("скажи чему равно 2 + 2 -> "))
res = 4
print("верно !" if num == res else " :( ")

numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for i in numbers:
    print(i, end=" ")

print()

for _ in numbers:
    print(" - ", end="")
# если нам не важна переменная, то ставим символ "_"

print()
num = int(input("Введите число для последовательности: "))
print(f"Последовательность от 0 до {num} с шагом 2 -> ", end="")
for i in range(0, num + 1, 2):
    print(i, end=" ")

print()
animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
# start=test в цикле используется для начала нумерации
for i, animal in enumerate(animals, start=1):
    animal = animal.replace("a", "A")
    print(i, animal)

print(animals)
# сам список не изменился


for i in range(len(animals)):
    animals[i] = animals[i].replace("a", "A")
print(animals)
# этим циклом мы изменили список
