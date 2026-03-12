import sys, keyword

print('Версия Python:', sys.version)
print('\nМестонахождение интерпритатора Python: ', sys.executable)
print('\nПуть поиска модулей Python: ')
for folder in sys.path:
    print(folder)

print('\nКлючевые слова Python: ')
for word in keyword.kwlist:
    print(word)