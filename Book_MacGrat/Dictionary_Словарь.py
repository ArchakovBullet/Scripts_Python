# Словарь: структура данных, 
# где элементы хранятся в виде пар ключ:значение

info = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}

print('info = ', type(info))

print('Словарь ', info)

print('\nСправочник ', info['ref'])
print('\nСправочник ', info['name']) 
print('\nСправочник ', info['sys'])

# Поиск конкретного ключа
print('\nЕсть ли здесь ключ name ?', 'name' in info)

# Вывод всех ключей словаря:
print('\nКлючи: ', info.keys())

del info['name']
info['user'] = 'Tom'
print('\nСловарь: ', info)

# Поиск конкретного ключа
print('\nЕсть ли здесь ключ name ?', 'name' in info)