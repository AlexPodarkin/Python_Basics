import logging

logging.basicConfig(filename='project.log', filemode='a+', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Основной файл проекта')


logger.debug(' Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')
