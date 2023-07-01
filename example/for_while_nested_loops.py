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


# m, n = list(map(int, input("Введите M и N через пробел(цифры) -> ").split()))
# arr = []
# for i in range(m):
#     arr.append([0] * n)
# print(arr)

n = list(map(int, input("Введите M и N через пробел(цифры) -> ").split()))
print(n)
