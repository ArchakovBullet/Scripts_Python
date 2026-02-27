'''
# import random # импортировали библиотечный класс random
# num = random.randint(1,15)
# flag = True
# quess = 0
# print('\nИгра отгадай число')
# print('Укажи число от 1 до 15', end=' ')
# while flag:
#     quess= input()
#     if not quess.isdigit():
#         print("Ошибка! Вводите только числа от 1 до 15")
#         break
#     elif int(quess) < num:
#         print("Слишко мало, попробуйте еще раз: ", end=' ')
#     elif int(quess) > num:
#         print('Слишком много, попробуйте еще раз', end=' ')
#     else:
#         print(f'Правильно, мое число  {quess}')
#         flag= False
'''
# Deep Seek подсказал как сделать проверку и на буквы и на числа диапазона:

import random

num = random.randint(1,15)
flag = True
quess = 0

print('\nИгра Угадай Число')
print('Укажи число от 1 до 15 ---> ', end=' ')

while flag:
    quess = input()
    # print(f'{quess} является ', type(quess))

    #Проверка, состоит ли строка из цифр.
    if not quess.isdigit():
        print('Ошибка! Вводите только числа.\nПопробуйте еще раз: ', end= ' ')
        continue # Перезапускаем цикл.

    # Проверяем, входит ли число в указанный диапазон 
    value = int(quess)
    if value < 1 or value > 15:
        print('Ошибка!!! Число должно быть в диапазоне от 1 до 15.\nПопробуйте еще раз.', end= ' ')
        continue # Перезапускаем цикл.

    # Сравниваем с заданным числом.
    if value < num:
        print('Слишком мало, попробуйте еще раз', end=' ')
    elif value > num:
        print('Слишком много, попробуйте еще раз', end=' ')
    else:
        print(f'В яблочко. Число угадано = {quess}')
        flag = False

