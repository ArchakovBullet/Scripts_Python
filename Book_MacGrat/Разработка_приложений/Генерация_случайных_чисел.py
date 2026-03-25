from random import random, sample

num = random()
print('Случайное число с плавающей точкой 0.0-1.0: ', num)

num = int(num * 10)
print('\nСлучайное целое число 0-9: ', num)

nums = []; i = 0
while i < 6:
    nums.append(int(random() * 10 ) + 1)
    i += 1

print('\nШесть случайных чисел от 1-10 : ', nums)

nums = sample(range(1,60), 6)
print('\nШесть случайных чисел от 1-59 : ', nums)

