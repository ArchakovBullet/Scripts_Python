# Сортировка пузырьком.

def buble_sort(array):
    for index in range(len(array)):
        for element in range((len(array) - 1) - index):
            if array[element] > array[element + 1]:
                array[element], array[element + 1] =\
                      array[element+1], array[element]
                print('\tРассматривается элемент [', element,\
                      '] to', array)

array = [5,3,1,2,6,4]
print('Сортировка пузырьком по книге \nМассив: ', array)
buble_sort(array)
print('Массив: ', array)

# Это сортировка пузырьком от Deep Seek.
def bubble_sort(arr):
    n = len(arr)
    # Проходим по массиву n-1 раз
    for i in range(n - 1):
        # Флаг для оптимизации (если массив уже отсортирован)
        swapped = False
        
        # Последние i элементов уже на месте
        for j in range(n - 1 - i):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Если не было обменов, массив отсортирован
        if not swapped:
            break
        
        # print(f"Проход {i + 1}: {arr}")
    
    return arr


# Тестируем
array = [5, 3, 1, 2, 6, 4]
print("\nСортировка пузырьком от DeepSeek\nИсходный массив:", array)
sorted_array = bubble_sort(array.copy())  # Используем copy(), чтобы не изменять оригинал
print("Отсортированный:", sorted_array)

# Пузырьковая сортировка - отличный учебный пример для понимания алгоритмов, 
# но никогда не используйте её в реальном коде. 
# Всегда пользуйтесь встроенной sorted() или list.sort()

import time

# Создаем массив из 1000 элементов
test_array = list(range(1000, 0, -1))  # Убывающий массив

# Встроенная сортировка
start = time.time()
sorted(test_array)
print(f"\nTimsort: {time.time() - start:.6f} сек")

# Пузырьковая сортировка (очень медленно!)
start = time.time()
bubble_sort(test_array.copy())
print(f"Пузырьковая: {time.time() - start:.6f} сек")