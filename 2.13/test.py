import logging

# Настройка логирования с пользовательским форматом времени
logging.basicConfig(filename='example.log', level=logging.DEBUG,
                    format='[%(asctime)s][%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S',  # Формат времени
                    encoding='utf-8')

# Запись логов
logging.debug('Это отладочное сообщение')
logging.info('Это информационное сообщение')
logging.warning('Это предупреждающее сообщение')
logging.error('Это сообщение об ошибке')
logging.critical('Это критическое сообщение')   
