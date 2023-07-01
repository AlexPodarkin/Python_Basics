s = 0
i = 1
n = 1000

while i <= n:
    s += i
    i += 1
print("summ = ", s)
# оператор < работает быстрее чем <=
# поэтому если есть возможность лучше использовать "<" ">" "==" "!="
# справка )

pass_true = "pass"
password = ""
while pass_true != password:
    password = input("Введите пароль -> ")
print("доступ разрешен !")

