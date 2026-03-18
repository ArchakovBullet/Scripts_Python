from Software_Class_Bird import*

print('\nЭкземпляры класса:\n', Bird.__doc__)

polly = Bird('Курлык-курлык')

print('\nКоличество птиц: ', Bird.count)
print('Полли говорит: ', polly.talk())

harry = Bird('Чирик-чирик')
print('\nКоличество птиц: ', Bird.count)
print('Гарри говорит: ', harry.talk())
