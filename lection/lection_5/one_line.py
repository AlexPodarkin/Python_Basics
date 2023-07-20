a, b, c = {"один", "два", "три"}
print(f'{a = } { b = } {c = }')

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь"]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-op\
tonal-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')
print(prefix + suffix)
