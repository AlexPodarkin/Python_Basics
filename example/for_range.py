arr = [1, 2, 3, 4, 5]

for i in arr:
    print(str(i), end=" ")

print()
for x in "Python":
    print(str(x), end=" ")

print()

summ = 0
for i in arr:
    summ += i
print("summ = ", summ)

for i in range(len(arr)):
    arr[i] = 5
print(arr)

print(list(range(5)))
# что такое range

s = 0
for i in range(2, 1001):
    s += 1 / i
print("s = ", s)

print("python".replace("p", "P"))
