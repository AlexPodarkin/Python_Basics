Документация к модулю работы с простыми числами
===
Описание функции is_prime()
---
Для проверки числа на простоту используйте функцию is_prime
модуля prime. Импортируйте её в свой код.

    >>> from doctest_python import is_prime

Теперь можно проверять 

    >>> is_prime(2)

    True

Функция использует остаток от деления

    >>> is_prime(100000007)
    If the number P is prime, the check may take a long time.Working...
    True
