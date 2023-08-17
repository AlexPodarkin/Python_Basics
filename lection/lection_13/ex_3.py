# Ключевое слово raise

num = 15
input_user = int(input('Введите  число: '))
if input_user == 0:
    raise ValueError('на ноль делить нельзя !')
else:
    num = num / input_user
print(f'ответ: {num}')
