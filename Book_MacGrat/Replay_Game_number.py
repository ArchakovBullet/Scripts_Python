
# Делаю повтор программы; "Угадай число."
'''''

import random
# Создаю переменные.
num = random.randint(1,10)
flag = True
quess = 0

print('Выбери число от 1 до 10 -->', end= '  ')

# Условия.
while flag:
    quess = input() # Принимает значение введенного числа


# Проверка, если введенное значение не является числом
    if not quess.isdigit():
        print('Внимание, ОШИБКА!! Введеное значение должно быть числом.\nВведите число ==>', end=' ')
        continue

# Преобразование переменной quess в int_переменную
    value = int(quess)

# Проверка, если значение меньше или больше заданного диапазона.
    if value < 1 or value > 10:
         print('Значение выбрано ВНЕ ДИАПАЗОНА.\nВведите значение в указанном диапазоне -->', end=' ')
         continue

    if value > num:
        print('Слишком много, попробуйте еще раз: ', end=' ')
    elif value < num:
        print('Слишко мало, попробуйте еще раз: ', end=' ')
    else:
        print(f'Значение угадано. Это число {num}')
        flag = False
'''

# Делаю еще раз повтор "Угадай число."
# Сделать счетчик попыток. P.S - Выполнено.
'''''
import random

number = random.randint(1,10)
flag = True
value = 0

# Счетчик попыток.
count = 0

print("Введите значение от 1 до 10 --> ", end=' ')

while flag:
    value = input()

    count += 1
    print(f'\nПопытка №  {count}')

    if not value.isdigit():
        print('ОШИБКА!!! Значение введено не корректно.\nВведите цифровое значение --> ', end=' ')
        continue

    valueInt = int(value)

    if valueInt < 1 or valueInt > 10:
        print('Значение введено ВНЕ ДИАПАЗОНА.\nВведите другое значение --> ', end=' ')
        continue
     
    if valueInt > number:
        print('Слишком много.Попробуйте еще раз --> ', end=' ')
    elif valueInt < number:
        print('Слишком мало.Попробуйте еще раз ---> ', end=' ')
    else:
        print(f'В ТОЧКУ. Сгенерированное число = {number}')
        flag = False
'''''

# Еще разок повтор Угадай число -- 23.02.2026 г.
'''''
import random

number = random.randint(1,10)
flag = True
value = 0

print('Уже третий повтор.\nВведите значение от 1 до 10 --> ', end=' ')

while flag:
    value = input()

    if not value.isdigit():
        print('Ошибка. Введены не цифровые значения.\nПопробуйте еще --> ', end=' ')
        continue

    num = int(value)
    if num < 1 or num > 10:
        print('Введенное значение ВНЕ ДИАПАЗОНА.\nВведите значение еще раз', end=' ')
        continue

    if num > number:
        print('Слишком много.Попробуйте еще --> ', end=' ')
    elif num < number:
        print('Слишком мало.Попробуйте еще разочек --> ',end='  ')
    else:
        print(f'В точку. Значение {number} угадано.')
        flag = False

'''''

# И еще разок 24.02.2026.
'''''
import random

num = random.randint(1,10)
flag = True
value = 0

print('Введите значение от 1 до 10 -- >  ', end=' ')

while flag:


    value = input()

    # Проверка,что нет букв.
    if not value.isdigit():
        print('Ошибка Ввода.Введите еще раз значение --> ', end=' ')
        continue
    # Проверка указанного диапазона
    valueNum =int (value)
    if valueNum < 1 or valueNum > 10:
        print("Значение вне указанного диапазона.\nПопробуйте еще раз --> ",end=' ')

    if valueNum < num:
        print('Слишком мало.Попробуйте еще раз --> ', end=' ')
    elif valueNum > num:
        print('Слишком много.Попробуйте еще разок --> ', end=' ')  
    else:
        print('Число угадано!!!')  
        flag = False
'''''

# Еще раз 25.02.2026
'''''''''
import random

number = random.randint(1,10)
flag = True
value = 0

print('Введите значение от 1 до 10 -> ', end=' ')

while flag:
    value = input()

    if not value.isdigit():
        print('Ошибка.Значение должно быть числовым.\nПопробуйте еще раз => ',end=' ')
        continue
    
    num = int(value)
    if num < 1 or num > 10:
        print('Ошибка.Значение вне диапазона.\nПопробуйте еще раз -> ',end=' ')
        
    
    if num < number:
        print('Слишком мало.Попробуйте еще разок --> ',end=' ')
    elif num > number:
        print('Слишком много.Попробуйте еще разочек -> ',end=' ')
    else:
        print('В яблоко. Значение угадано.')
        flag = False
'''
# и еще разок 25.02.2026 
'''''''''
import random

number = random.randint(1,10)
flag = True
value = 0

print('Введит значение от 1 до 10 --> ', end=' ')

while flag:
    value = input()

    if not value.isdigit():
        print('Ошибка.Значение не цифровое.Попробуйте еще разочек: ', end=' ')
        continue

    value_int = int(value)

    if value_int < 1 or value_int > 10:
        print('Ошибочка.Значение вне диапазона.Попробуйте еще раз --', end=' ')
        continue

    if value_int < number:
        print('Слишком мало.Попробуйте еще разочек --> ',end=' ')
    elif value_int > number:
        print('Слишком много.Попробуйте еще раз -> ',end=' ')
    else:
        print('Отлично сработано.')
        flag=False
'''

# Еще раз 28.02.2026 года.
'''''''''
import random

number = random.randint(1,10)
flag = True
value = 0

print('Введите значение от 1 до 10 -->  ', end=' ')

while flag:
    value = input()

    if not value.isdigit():
        print('Ошибка.Не числовое значение.Попробуйте еще раз --> ', end=' ')
        continue
    
    valueInt = int(value)

    if valueInt < 1 or valueInt > 10:
        print('Введенное значение Вне диапазона.Попробуй еще раз --> ', end=' ')
        continue

    if valueInt < number:
        print('Слишком мало.Попробуй еще --> ', end=' ')
    elif valueInt > number:
        print('Слишком много.Попробуй еще --> ', end=' ')
    else:
        print('Отличная работа.Число ', number,'классно отработано.')
'''

