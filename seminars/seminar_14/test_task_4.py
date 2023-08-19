# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
# P.S. ФАЙЛ ОБЯЗАТЕЛЬНО ДОЛЖЕН НАЧИНАТЬСЯ СО СЛОВА test_

import pytest
from task_2 import removal


def test_ret_same():
    assert (removal('language') == 'language')


def test_lower():
    assert (removal('Lan$gu$agE') == 'language')


def test_punt():
    assert (removal('l,an.gu:a!g?e') == 'language')


def test_non_rus():
    assert (removal('lфa$ngu$age') == 'language')


def test_non_all():
    assert (removal('Lфв,an.gu:a!g?E') == 'language')


if __name__ == 'main':
    pytest.main(['-v'])
