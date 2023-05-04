# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging

FORMAT = '{levelname} - {asctime} - {funcName}->{lineno}:{msg}'
logging.basicConfig(level=logging.INFO, filename='deco1.log', encoding='utf-8',format = FORMAT, style="{")
logger = logging.getLogger(__name__)

def deco_file(func):

    def wrapper(*args, **kwargs):
        data = []
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        print(new_data)
        logger.info(f' {func.__name__}{new_data}')
        return result
    return wrapper
@deco_file
def call(*args, **kwargs):
    pass
call(12, 24, 56, ax = 12, b = 45)