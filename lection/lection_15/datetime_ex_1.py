from datetime import time, date, datetime
from datetime import timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0, microsecond=24)
print(f'{d = }\t-\tstr: {d}')
print(f'{t = }\t-\tstr: {t}')
print(f'{dt = }\t-\tstr: {dt}')

date_ = date(year=2007, month=6, day=15)
print(f'Ткущая дата: {date_}')
time_ = time(hour=2, minute=14, second=0)
print(f'Время: {time_}')

# Ещё один важный тип данных — timedelta. Объект представляет собой разницу во
# времени между различными датами и временными промежутками.
# Простой пример создания временной разницы:
delta = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(f'{delta = }\t-\t{delta}')
print(type(delta))

# В отличие от трёх временных типов, дельты могут принимать на вход любые
# числовые значения. Например, количество минут может быть больше 60. Кроме того
# дельта может быть отрицательной.
delta = timedelta(weeks=53, days=500, hours=73, minutes=101, seconds=303, milliseconds=67890, microseconds=1234567)
neg_delta = timedelta(days=-3, minutes=-42)
print(f'{delta = }\t-\t{delta}')
print(f'{neg_delta = }\t-\t{neg_delta}')
