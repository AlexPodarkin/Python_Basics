# Классы bytes и bytearray
text_en = "Hello Alex !"
res = text_en.encode('utf-8')
print(res, type(res))

text_ru = 'Привет, Александр !'
res = text_ru.encode("utf-8")
print(res, type(res))

print("-" * 50)
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')
