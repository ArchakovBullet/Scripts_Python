# global_var =1

# def my_vars():
#     print('Глобальная переменная global_var\t', global_var)
#     local_var = 2
#     print('Локальная переменная  local_var\t', local_var)
#     global inner_var
#     inner_var = 3


# my_vars()
# print('Вторая глобальная переменная global inner_var\t', inner_var)

# Добавление параметров в функцию.
# def echo(user, lang, sys):
#     print('\nПользователь: \t', user, '\nЯзык: \t\t', lang, '\nПлатформа: \t', sys)

# echo('Mike', 'Python', 'Windows')


#  Мой пример:
# def whoayou(name, town):
#     print('Это ', name, '\nОн из города ', town)


# my_name = input('Введите имя ')
# my_town = input ( 'Введите город ')

# whoayou (my_name, my_town)

# Пример Алиса_1  Функция с одним параметром
# def greet(name):
#     print(f"Привет, {name}!")

# # Вызов функции
# greet("Анна")  # Вывод: Привет, Анна!
# greet("Иван")  # Вывод: Привет, Иван!


#  Пример Алиса_2 Функция с несколькими параметрами
# def calculate_area(length, width):
#     area = length * width
#     return area

# rezult =  calculate_area(5, 3)
# print(f'Площадь прямоугольника = {rezult}')

#  Функция с параметрами по умолчанию
# def send_email(to, subject = 'Без темы', boby = 'Пустое сообщение'):
#     print('\n1_Кому:', to, subject)
#     print('\n2_Тема: ', subject)
#     print('\n3_Текст: ',boby)
#     print(to, subject, boby)

# send_email('user_player')
# send_email('user', 'Все важно')
# send_email('player', 'Тема', 'Не для слабых духом')

# Функция с произвольным числом позиционных аргументов (*args)
# def sum_numbers(*args):
#     total = sum(args)
#     return total

# print(sum_numbers(1,2,3))
# print(sum_numbers(10,20,30,40))
# print(sum_numbers())

#  Функция с произвольным числом именованных аргументов (**kwargs)
# def print_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Вызов функции
# print_user_info(name="Мария", age=25, city="Москва")
# # Вывод:
# # name: Мария
# # age: 25
# # city: Москва

# #  Комбинированный пример (*args и **kwargs)
# def flexible_function(required_param, *args, **kwargs):
#     print(f"Обязательный параметр: {required_param}")
#     print(f"Дополнительные позиционные аргументы: {args}")
#     print(f"Именованные аргументы: {kwargs}")

# # Вызов функции
# flexible_function(
#     "обязательный",
#     "доп1", "доп2",
#     name="Алексей", age=30
# )
# Вывод:
# Обязательный параметр: обязательный
# Дополнительные позиционные аргументы: ('доп1', 'доп2')
# Именованные аргументы: {'name': 'Алексей', 'age': 30}

# Как я понимаю функцию
def known (value_1 = 10, value_2 = 55, value_3 = 100):
    print(value_1, value_2, value_3)

known()
known(22, 15)
known(12, 70, 120) # Определенно мне пока что это понятно !!!