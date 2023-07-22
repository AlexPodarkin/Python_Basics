from sys import argv
from datetime import datetime

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


def check_data(date_text):
    """Модуль с проверкой даты"""
    *_, year = list(date_text.split("."))
    try:
        print(date_text)
        datetime.strptime(date_text, "%d.%m.%Y").date()
        check_year(int(year))
        return True
    except ValueError:
        print("Некорректная дата")
        return False


def check_year(year):
    """Модуль с проверкой високосного года"""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Високосный год")
    else:
        print("не високосный год")


if __name__ == '__main__':
    print("Запускать через консоль (передать дату ДД.ММ.ГГ) !!!")
    print(check_data(*(argv[1:])))
