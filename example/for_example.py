# a = test
# n = int(input("Введите число для вычисления факториала -> "))
# for i in range(test, n + test):
#     a *= i
# print(a)

for i in range(1, 7):
    print("*" * i)

words = ["Python", "very", "like", "hello"]
words = " ".join(words)
print(words)

# еще вариант
words = ["Python", "very", "like", "hello"]
res = ""
for i in range(len(words)):
    res += words[i] + " "
print(res)

# еще вариант
words = ["Python", "very", "like", "hello"]
res = ""
for w in words:
    res += w + " "
print(res.rstrip())
# rstrip() - убрал последний ненужный пробел !


digs = [1, 23, 54, 564, 21, 0, 2, 5, 12, 32]
# цикл с использованием enumerate
for i, d in enumerate(digs):
    if 10 <= d <= 99:
        digs[i] = 0
print(digs)
#  мы получаем значение "d" и индекс "i"


print(ord("s"))
# функция ord() показывает код буквы
