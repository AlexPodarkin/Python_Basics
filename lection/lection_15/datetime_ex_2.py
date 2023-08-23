# Математика с датами
from datetime import datetime, timedelta, time, date

date_1 = datetime(2012, 12, 21)
date_2 = datetime(2017, 8, 19)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')
print(type(date_2))
print(type(delta))
birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')

# Доступ к свойствам
d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
delta = timedelta(weeks=53, hours=73, minutes=101, seconds=303, milliseconds=60)
print(f'{d.month}')
print(f'{t.second}')
print(f'{dt.hour}')
print(f'{delta.days}')

# Изменить значение напрямую не получится. Всё же перед нами неизменяемые
# объекты. Но мы можем воспользоваться методом replace для создания копии со
# значениями текущего объекта. Изменения затронут только указанные параметры.
new_dt = dt.replace(year=2012)
one_more_hour = t.replace(t.hour + 1)
print(f'{new_dt}\n{one_more_hour}')
