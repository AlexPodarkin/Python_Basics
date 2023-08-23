import logging

FORMAT = '{levelname:<8} | {asctime}. В модуле"{name}" в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд,| сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)

logger = logging.getLogger(__name__)
logger.debug(' Очень подробная ')
logger.info('Немного информации')
logger.warning('Внимание! ')
logger.error('Поймали ошибку. ')
logger.critical('На этом всё')
