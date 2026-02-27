basket = ['Яблоко','Булочка','Кола']
crate = ['Яйцо','Инжир','Виноград']

print('\nСписок basket:', basket)
print('Элементов в списке basket: ', len(basket))

basket.append('Чернослив')
print('\nДобавлено: ', basket)
print('Элементов в списке basket: ', len(basket))

# print('\nПоследний удаленный элемент: ', basket.pop())
# print('Список basket: ', basket)

# print(crate)
basket.extend(crate)
print('Добавлен второй список: ', basket)
print('Элементов в списке basket: ', len(basket))

# Удаление элемента по индексу.
del basket[1]
print('\nУдалили элемент "Булочка": ', basket)

del basket[1:3]
print('Срез удален: ', basket)