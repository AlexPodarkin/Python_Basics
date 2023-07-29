a = int(input("введите test число: "))
b = int(input("введите 2 число: "))
c = int(input("введите 3 число: "))

if a > b:
    if a > c:
        print("test число больше")
    elif a == c:
        print("1e & 3e max")
    else:
        print("3 число больше")
elif a == b == c:
    print("все числа равны")
else:
    if b > c:
        if a == b:
            print("1e & 2e max")
        else:
            print("2 число больше")
    elif b == c:
        print("2e & 3e max")
    else:
        print("3 число больше")

#
# if a > b and a > c:
#     print("test число больше")
# if b > a and b > c:
#     print("2 число больше")
# if c > a and c > b:
#     print("3 число больше")
