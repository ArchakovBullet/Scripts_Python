# # Создан текст.
poem ='Скажи-ка, дядя, ведь недаром\n'
poem+='Москва, спаленная пожаром,\n'
poem+='Французу отдана?\n'
poem+='Ведь были ж схватки боевые,\n'
poem+='Да, говорят, еще какие!\n'
poem+='Недаром помнит вся Россия\n'
poem+='Про день Бородина!\n'

# Создан файл и в него записан текст --> w
file = open('e:/Python/My_Scripts_Python/Book_MacGrat/stish_Lermontov.txt', 'w')
file.write(poem)
file.close()

# # Открыт файл для чтения --> r
# file = open('e:/Python/My_Scripts_Python/Book_MacGrat/stish_Lermontov.txt', 'r')
# # Выведен текст на экран.
# for line in file:
#     print(line, end='')
# file.close()

# В текстовый файл ДОБАВЛЕН автор произведения --> a
file = open('e:/Python/My_Scripts_Python/Book_MacGrat/stish_Lermontov.txt', 'a')
file.write('  (Михаил Лермонтов.)', )
file.close()

# Теперь выводим все в печать.
file = open('e:/Python/My_Scripts_Python/Book_MacGrat/stish_Lermontov.txt', 'r')
for line_avtor  in file:
    print(line_avtor, end=' ')
file.close()

# Код от Deep Seek
# Создан текст.
# poem = 'Скажи-ка, дядя, ведь недаром\n'
# poem += 'Москва, спаленная пожаром,\n'
# poem += 'Французу отдана?\n'
# poem += 'Ведь были ж схватки боевые,\n'
# poem += 'Да, говорят, еще какие!\n'
# poem += 'Недаром помнит вся Россия\n'
# poem += 'Про день Бородина!'

# # Используем локальный файл в той же папке, где запущен скрипт
# filename = 'stish_Lermontov.txt'

# # Запись в файл
# file = open(filename, 'w', encoding='utf-8')
# file.write(poem)
# file.close()
# print("Файл создан и текст записан")

# # Чтение из файла
# file = open(filename, 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()
# print("\nЧтение завершено")

# # Добавление автора
# file = open(filename, 'a', encoding='utf-8')
# file.write('\n(Михаил Лермонтов.)')
# file.close()
# print("Автор добавлен")

# # Проверим результат
# file = open(filename, 'r', encoding='utf-8')
# print("\nИтоговое содержимое файла:")
# print(file.read())
# file.close()

# Еще более усовершенствованный код, исключающий ошибки, от Deep Seek
# Этот способ гарантирует закрытие файла даже в случае ошибок.
# Создан текст.
# poem = 'Скажи-ка, дядя, ведь недаром\n'
# poem += 'Москва, спаленная пожаром,\n'
# poem += 'Французу отдана?\n'
# poem += 'Ведь были ж схватки боевые,\n'
# poem += 'Да, говорят, еще какие!\n'
# poem += 'Недаром помнит вся Россия\n'
# poem += 'Про день Бородина!'

# filename ='e:/Python/My_Scripts_Python/Book_MacGrat/stish_Lermontov_Great.txt'

# # Запись
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(poem)

# # Чтение
# with open(filename, 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')

# # Добавление
# with open(filename, 'a', encoding='utf-8') as file:
#     file.write('\n(Михаил Лермонтов.)')

# # Проверка
# with open(filename, 'r', encoding='utf-8') as file:
#     print("\n\nФинальный текст:")
#     print(file.read())