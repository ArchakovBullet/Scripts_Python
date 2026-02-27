num1 = input('Введите первое значение --> ')
num2 = input('Введите второе значение --> ')

total = num1 + num2
print(f'Вывод = {total} --> {type(total)}\n')

print('Значения преобразованы в int')
total = int(num1) + int(num2)
print(f'Вывод = {total} --> {type(total)}\n')


num1 = input('Введите первое значение --> ')
num2 = input('Введите второе значение --> ')
print('Одно значение преобразовано в float, второе во float')
total = float(num1) + float(num2)
print(f'Вывод = {str(total)} --> {type(total)}')# В том смысле, что str не может преобразовать float

