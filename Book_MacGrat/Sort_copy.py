# Сортировка с копированием.(стр. 88)
# def copy_sort(arraylen):
#     copy = arraylen[:]
#     sorted_copy= []

#     while len(copy) > 0:
#         minimum = 0
#         for element in range(1, len(copy)):
#             if copy[element] < copy[minimum]:
#                 minimum = element
#         print('\tУдаляем ', copy[minimum], 'Из', copy)
#         sorted_copy.append(copy.pop(minimum))
    
#     return sorted_copy

# array = [5,3,1,2,6,4]
# print('Сортировка с копированием ....\nМассив: ', array)

# print('Копия:', copy_sort(array))
# print('Массив:', array)


# В Python есть несколько встроенных методов сортировки, которые работают похожим образом:
# 1
# array = [5,3,1,2,6,4]
# sorted_array = sorted(array)
# print('\nСортировка: ', sorted_array)
# print('Оригинал неизменен: ', array)

# 2 Сортирует список на месте.
# array = [5,3,1,2,6,4]
# array.sort() # Сортирует исходный список
# print(array) # [1, 2, 3, 4, 5, 6] - оригинал изменился

# Реализация учебника - отличный учебный пример для понимания алгоритмов сортировки, 
# но в реальных проектах всегда лучше использовать встроенные методы Python.