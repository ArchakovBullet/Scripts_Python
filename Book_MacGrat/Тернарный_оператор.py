
'''''

a = input()
b = input()

# Тернарный оператор.
total= a if(a>b) else b

print(type(a),type(b),'= ', total)

c = 10

# Также тернарный оператор. 
total2 =int (a) if (int(a)>c) else c
print(type(int(a)),type(c),'= ', total2)
print(type(total2))
'''

# Продолжение тематики тернарного оператора. PS - это мой код. Несколько некорректно работает при 
# вводе неправильных значений.
'''''''''
flag = True
# Защита от дурака
while flag:
    print('Ввод первого значения --> ', end=' ')
    a = input()

    if not a.isdigit():
        print('Ввод  1 значения некорректен.\nПопробуйте еще раз --> ')
        continue


    print('Ввод второго значения --> ', end=' ')
    b = input()

    if not b.isdigit():
        print('Ввод 2 значения некорректен.\nПопробуйте еще раз --> ')
        continue

    # А вот и сам тернарный оператор.
    total =int(a) if int(a) > int(b) else int(b)

    print(f'Кто из чисел больше ? {a} или {b} ? Ответ: {total}')
    flag = False

'''

# Это исправленный код Deep Seek
'''''''''
flag = True
a = None
b = None

while flag:
    # Ввод первого числа
    if a is None:  # Запрашиваем только если еще не ввели
        print('Ввод первого значения --> ', end=' ')
        a_input = input().strip()
        
        # Проверка на отрицательное число
        if a_input.startswith('-') and a_input[1:].isdigit():
            a = int(a_input)
        elif a_input.isdigit():
            a = int(a_input)
        else:
            print('Ввод 1 значения некорректен. Введите целое число.')
            continue
    
    # Ввод второго числа
    if b is None:  # Запрашиваем только если еще не ввели
        print('Ввод второго значения --> ', end=' ')
        b_input = input().strip()
        
        # Проверка на отрицательное число
        if b_input.startswith('-') and b_input[1:].isdigit():
            b = int(b_input)
        elif b_input.isdigit():
            b = int(b_input)
        else:
            print('Ввод 2 значения некорректен. Введите целое число.')
            continue
    
    # Если оба числа введены корректно
    total = a if a > b else b
    print(f'Кто из чисел больше ? {a} или {b} ? Ответ: {total}')
    flag = False
'''

# А вот еще более компактный код от Deep Seek

def get_number(prompt):
    """Функция для безопасного ввода числа"""
    while True:
        print(prompt, end=' ')
        value = input().strip()
        
        # Проверка на отрицательное число
        if value.startswith('-') and value[1:].isdigit():
            return int(value)
        elif value.isdigit():
            return int(value)
        else:
            print('Ошибка! Введите целое число.')

# Основная программа
print("Сравнение двух чисел")
a = get_number('Ввод первого значения -->')
b = get_number('Ввод второго значения -->')

total = a if a > b else b
print(f'Кто из чисел больше ? {a} или {b} ? Ответ: {total}')


