print('Замыкание')


def say_name(text):
    def say_bye():
        print(f"Alex, {text}")

    return say_bye


print('Мы получили функцию (т.е вернули ссылку на внутреннюю функцию)', say_name('Goodbye'))
func_say_bye = say_name('Goodbye')
print("Мы сохранили этот ссылку на функцию в переменную 'func_say_bye' и теперь можем ее вызвать(код ниже)")
func_say_bye()

func_say_bye_2 = say_name('Hi ')
func_say_bye_2()
print("func_say_bye_2 - создается свое независимое локальное окружение ")


def counter(start=0):
    def func():
        nonlocal start
        start += 1
        return start

    return func


print("так мы можем создавать независимые счетчики")
counter_1 = counter(10)
counter_2 = counter()
print(f'первый счетчик = {counter_1()}, второй счетчик = {counter_2()}')
print(f'первый счетчик = {counter_1()}, второй счетчик = {counter_2()}')
print(f'первый счетчик = {counter_1()}, второй счетчик = {counter_2()}')


def strip_text(char=" "):
    def strip(text):
        nonlocal char
        return text.strip(char)

    return strip


text_strip = strip_text()
text_strip_2 = strip_text("1,2,3")
print(text_strip("   Hi!   "))
print(text_strip_2("Hi!    123"))

