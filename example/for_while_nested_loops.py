for i in range(1, 4):
    print(f"i = {i}")
    for j in range(1, 6):
        print(f"j = {j}", end=" ")
    print()
print("\n\n")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"i = {i}, j = {j}", end=" ")
    print()

m, n = list(map(int, input("Введите M и N через пробел(цифры) -> ").split()))
array = []
print(m, n)
for i in range(m):
    array.append([0] * n)
print(array)

count = 0
for i in range(m):
    for j in range(n):
        count += 1
        array[i][j] = count

for i in array:
    print(" - ".join([str(k) for k in i]))
# для красивого вывода 2-х мерного массива надо пробежаться по нему
# преобразовав все в строку [str(k) for k in i] и воспользовавшись методом " - ".join вывести на печать


