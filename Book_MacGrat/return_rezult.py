def add_sum(a,b):
    c= a+b
    return c


try:
    value1=int (input ('Введите первое значение --> ')) 
    value2=input('Введите второе значение --> ')
    rezult = add_sum(value1,int (value2))
    print(rezult)
except ValueError:
    print('Ошибка.Введите целое число.')

# # Пример прерывания функции.
# def summe(x, y):
#     if x < 6:
#         return
#     return x*y

# rez = summe(5, 6)
# print('\n',rez)

# Пример:
# def squared (num: str):
#     flag = True
#     while flag:
#         if num.isdigit():
#             num = int(num)
#             return num, num * num
#         else:
#             print('Ошибка ввода.Попробуйте еще раз -->', end=' ')
#             num = input()

# # squared()
# num =input('Ввод числа ')
# num, rezult = squared(num)
# print(num, '*', num ,'=', rezult)

# Тот же пример с try/except

# def squared(num):
#     try:
#         num = int(num)
#         return num * num
#     except ValueError:
#         print('Ошибка ввода.')
#         return
# num =input('Ввод числа ')
# rezult = squared(num)
# print(num, '*', num ,'=', rezult)
