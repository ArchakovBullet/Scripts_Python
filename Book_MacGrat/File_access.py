# Доступ к файлам.

# def get_status(f):
#     if not f.closed:
#         return 'Открыт'
#     else:
#         return 'Закрыт'

# Если хотим, чтобы файл был создан в конкретной папке.

# file = open('e:/Python/My_Scripts_Python/Book_MacGrat/example.txt', 'w')
# print('Имя файла: ', file.name)
# print('Режим открытого файла : ', file.mode)
# print('Чтение: ', file.readable())
# print('Запись: ', file.writable())

# print('\nСтатус файла ', get_status(file))
# file.close()  # Нужны скобки! Было: file.close
# print('\nСтатус файла', get_status(file))


# Это код ниже от Deep Seek:

import os
# Файл будет создан в директории, где находится python
# file = open('example.txt', 'w')

file = open('e:/Python/My_Scripts_Python/Book_MacGrat/example.txt', 'w')

# Текущая директория   
current_dir = os.getcwd()
print("\nТекущая директория:", current_dir)

# Полный путь к файлу
full_path = os.path.join(os.getcwd(), 'e:/Python/My_Scripts_Python/Book_MacGrat/example.txt')
print("Полный путь к файлу:", full_path)


# import os

# print("\nСкрипт запущен из:", os.getcwd())

# file = open('example.txt', 'w')
# print("Файл создан в:", os.path.abspath(file.name))
# file.close()