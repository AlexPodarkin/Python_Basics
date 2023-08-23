# Мы можем использовать специальные методы для получения удобного вывода
# информации и наоборот, формировать объекты datetime из человеко читаемых строк.
from datetime import datetime

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
print(dt)
print(dt.timestamp())
# Timestamp — возвращаем время в секундах от начала времён. Под началом понимаем полночь 1 января 1970 года.
print(dt.isoformat())
# Iso format — выводит дату в формате, соответствующем стандарту ISO 8601. Это международный стандарт описывающий
# формат даты и времени и рекомендации по его использованию.
print(dt.weekday())
# weekday — позволяет получить день недели в виде целого числа, где 0 -
# понедельник, а 6 — воскресенье.
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S.Это %W неделя и %j день года.'))
# strftime — выводит дату в соответствии с переданным в виде str форматом.

# А теперь несколько обратных методов, позволяющих создать объекты datetime.
date_original = '2022-12-12 18:01:21.555470'
date_timestamp = 1181862840.000024
date_iso = '2007-06-15T02:14:00.000024'
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
original_date = datetime.fromisoformat(date_original)
timestamp_date = datetime.fromtimestamp(date_timestamp)
iso_date = datetime.fromisoformat(date_iso)
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(original_date)
print(timestamp_date)
print(iso_date)
print(text_date)

print(f'текущее время: {datetime.now().strftime("%H:%M:%S")}')
print(f'текущая  дата: {datetime.now().strftime("%d %B %Y")}')
text = '12:00:00 15 June 2009'
date_time = datetime.strptime(text, '%H:%M:%S  %d %B %Y')
print(date_time)
print(date_time.day)
