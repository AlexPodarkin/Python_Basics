import logging

logging.basicConfig(level=logging.NOTSET)
#  если не указать уровень logging.basicConfig, по умолчанию будет warning
logger = logging.getLogger(' LOG')
# В официальной документации указано, что работать с регистраторами
# напрямую запрещено. Необходимо использовать функцию уровня модуля
# logging.getLogger(name) для получения регистраторов.
# Вместо лога обычно используют имя программы __name__
logger.debug(' Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info(' Немного информации о работе кода')
logger.warning(' Внимание! Надвигается буря!')
logger.error(' Поймали ошибку. Дальше только неизвестность')
logger.critical(' На этом всё')
# По умолчанию логгер имеет следующие уровни журналирования
# ● NOTSET, 0 — уровень не установлен. Регистрируются все события.
# ● DEBUG, 10 — подробная информация, обычно представляющая интерес только при диагностике проблем.
# ● INFO, 20 — подтверждение того, что все работает так, как ожидалось.
# ● WARNING, 30 — указание на то, что произошло что-то неожиданное, или указание на какую-то проблему в ближайшем
# будущем (например, «недостаточно места на диске»). Программное обеспечение по-прежнему работает, как ожидалось.
# ● ERROR, 40 — из-за более серьезной проблемы программное обеспечение не может выполнять некоторые функции.
# ● CRITICAL, 50 — серьезная ошибка, указывающая на то, что сама программа не может продолжать работу