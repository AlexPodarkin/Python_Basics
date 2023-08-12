# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
import json


class Check:
    def __init__(self, name_full: str = None):
        self.name_full = name_full

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value: str):
        if not value.istitle():
            raise ValueError(f'Ошибка "{value}", ввод ФИО должен быть с большой буквы')
        if not all(i.isalpha() for i in value):
            raise TypeError(f'Ошибка "{value}", наличие только букв')


class Student:
    name = Check()
    surname = Check()
    patronymic = Check()
    grade_res = 'оценки'
    test_res = 'результаты тестирования'

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.study_journal = dict()
        with open('lesson_titles.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter="\n")
            for row in file_reader:
                self.study_journal[str(*row)] = {self.grade_res: [], self.test_res: []}

    def rate_student(self, subject: str, estimate: int):
        if not 1 < estimate < 6:
            raise ValueError('оценки (от 2 до 5)')
        self.study_journal[subject][self.grade_res].append(estimate)

    def test_score(self, subject: str, estimate: int):
        if not -1 < estimate < 101:
            raise ValueError('оценки (от 2 до 5)')
        self.study_journal[subject][self.test_res].append(estimate)

    def subject_average(self, subject):
        if self.study_journal[subject][self.grade_res]:
            result = sum(self.study_journal[subject][self.grade_res]) / len(self.study_journal[subject][self.grade_res])
            return f'Средняя оценка по предмету "{subject}": {result} балла.'
        return f'Средняя оценка по предмету "{subject}": оценки отсутствуют.'

    def test_average(self, subject):
        if self.study_journal[subject][self.test_res]:
            result = sum(self.study_journal[subject][self.test_res]) / len(self.study_journal[subject][self.test_res])
            return f'Средняя оценка тестирования по предмету "{subject}": {result} балла.'
        return f'Средняя оценка тестирования по предмету "{subject}": тестирование не проходил.'

    def overall_point_average(self):
        summ = 0
        count = 0
        for i in self.study_journal:
            if self.study_journal[i][self.grade_res]:
                summ += sum(self.study_journal[i][self.grade_res])
                count += len(self.study_journal[i][self.grade_res])
        return round(summ / count, 2)

    def __repr__(self):
        return f'Student(name={self.name}, surname={self.surname}, patronymic={self.patronymic})'


if __name__ == '__main__':
    vas = Student('Вася', 'Пупкин', 'Васильевич')
    print(vas)

    # оценки
    vas.rate_student('Геометрия', 5)
    vas.rate_student('Физическая культура', 5)
    vas.rate_student('Геометрия', 4)
    # vas.rate_student('Математика', 4)
    # vas.rate_student('Математика', 4)

    # тестирование
    vas.test_score('Геометрия', 95)
    vas.test_score('Геометрия', 100)

    # результат, оценки (средний балл)
    print(vas.subject_average('Геометрия'))
    print(vas.subject_average('Физическая культура'))
    print(vas.subject_average('Математика'))

    # результат, тестирование (средний балл)
    print(vas.test_average('Геометрия'))
    print(vas.test_average('Физическая культура'))

    print(f'Средний балл студента = {vas.overall_point_average()}')

    # для красоты)
    with open('оценки.json', 'w', encoding='utf-8') as file_json:
        json.dump(vas.study_journal, file_json, ensure_ascii=False, indent=4)
