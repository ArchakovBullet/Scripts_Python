# Типы данных.
#Логические значения (bool)
isMarried = False
print(isMarried)

isAlive = True
print(isAlive)

# Целые числа(int)
age = 21
print("Возраст =  ", age)

count = 15
print('Количество = ', count)

# Дробные числа (float)
heigt = 1.55
pi = 3.14
weight = 78.
print(heigt, pi, weight)

# Строки (str)
message = "Hello"
print(message)

name = 'Tommi'
print(name)

userName = 'Tom'
userAge = 33
user = f"name: {userName} \n age: {userAge} "
print(user)

# Димнамическая типизация.
userID ='ABC'# тип str
print(userID)

userID = 555 # int
print(userID)

# С помощью встроенной функции type() динамически можно узнать текущий тип переменной:
userID ='ABC'         # тип str
print(type(userID))   # <class 'str'>

userID = 777           # тип int
print(type(userID))    # <class 'int'>