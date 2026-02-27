
# Список
chars = ['A','B','C']

# Кортеж
fruit = ('Apple', 'Banana', 'Cherry')

# Словарь
info = {'name':'Mike', 'ref': 'Python', 'sys':'Win'}

print('Вывод элементов списка:\t ', end=' ')
for item in chars:
    print(item, end=' ')

# Вывод списка с индексами
print('\nВывод индексов значений списка:\t', end=' ')
for item in enumerate(chars):
    print(item, end='')

# Вывод элементов списка и кортежа
print('\nВывод значений списка и кортежа:\t', end=' ')
for item in zip(chars,fruit):
    print(item, end=' ')

# Вывод значений ключей словаря.
print('\nВывод словаря парами:\n', end='')
for key, value in info.items():
    print(key ,' = ',value)