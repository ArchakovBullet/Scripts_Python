#  Обращение к свойствам класса.
from Software_Class_Bird import*

chick = Bird('Пи-пи-пи')
chick.age = '1 неделя'

print('Цыпленок говорит: ', chick.talk)
print('Возраст цыпленка: ', chick.age)

chick.age = '2 недели.'
print('Возраст цыпленка: ', chick.age)

setattr(chick,'age','3 недели.')   

print('\nАтрибуты экземпляра chick....')
for attrib in dir(chick):
    if attrib[0] != '_':
        print(attrib,':', getattr(chick, attrib))

delattr(chick, 'age')
print('\nУ цыпленка есть атрибут возраста ?', hasattr(chick, 'age'))