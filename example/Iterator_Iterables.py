arr = [5, 3, 7, 10, 32]

print(iter(arr))
# получили итератор
it = iter(arr)
print(next(it), next(it), next(it))

s = "Python"
it = iter(s)
print(next(it), next(it), next(it))

r = range(5)
it = iter(r)
print(next(it), next(it), next(it))
