import math, random

print('Округление в большую сторону 9,5 : ', math.ceil(9.5), type(math.ceil(9.5)))
print('Округление в меньшую сторону 9,5 : ', math.floor(9.5), type(math.floor(9.5)))

num = 4
print('\nКвадрат : ', math.pow(num, 2), type(num))
print('Квадратный корень : ', math.sqrt(num), type(num))

# Случайный список из значений(от 1 до 60) из какого-то (10) количества значений.
number = random.sample(range(1,60), 10)
print('\nСлучайные числа -->  ', number, type(number))