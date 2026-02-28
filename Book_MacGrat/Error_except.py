'''''''''
title = 'Программирование для начинающих'

try:
    print(title)# Если заменить на ttitle, то возникнет исключение и код перейдет в блок except
except NameError as msg:
    print(msg)
'''''

# Можно обработать несколько исключений.

# Использование ключевого слова 'raise'
day = 32

try:
    if day > 31:
        raise ValueError('Неверный номер дня.')
except ValueError as msg:
    print('Прога нашла ошибку', msg)
finally:
    print('Но погода по настоящему супер.')