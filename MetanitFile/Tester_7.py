# Условные выражения
print ('Условные выражения')
firstNumber = 5
secondNumber = 6
print('5 == 6  = ', 5 ==6)
print('5 != 6  = ', 5 != 6)
print('5 > 6   = ', 5 > 6)
print('5 < 6   = ', 5 < 6)

# Логические операции
# x and y
print ('\nx and y')
age = 43
weight = 76
result = age > 40 and weight == 76
print('Оператор and = ', result)

# x or y
print ('\nx or y')
age = 43
weight = 76
result = age > 40 or age < 30
print('Оператор or = ', result)

# not (логическое отрицание)
# Возвращает True, если выражение равно False
print('\nВыражение not')
age = 22
isMarried = False
print(not age > 21)# False
print(not isMarried) # True
print(not 4) # False
print(not 0) # True

# Оператор in
# Оператор in возвращает True 
# если в некотором наборе значений есть определенное значение.
print('\nОператор in')
message = 'Hello World'
helloStr1 = 'Hello'
helloStr2 = 'hello'
print('Есть ли Hello в Hello World =  ', helloStr1 in message)
print('Есть ли hello в Hello World =  ', helloStr2 in message)

# Если нам надо наоборот проверить, 
# нет ли в наборе значений какого-либо значения, 
# то мы може использовать модификацию оператора - not in. 
# Она возвращает True, если в наборе значений НЕТ определенного значения
print('\nОператор not in')
message = 'Hello World'
helloStr = 'Hello'
print(helloStr not in message) # False
gold = 'Gold'
print(gold not in message) # True