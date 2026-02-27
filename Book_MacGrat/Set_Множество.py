# Множество - в Python это список уникальных элементов,
# где повторения не допускаются. 
# Это изменяемый набор уникальных значений, где повторения не допускаются.

# setPy = {'Alfa','Bravo', 'Charly'}
# print(setPy)
# print('Количество значений:',len(setPy))
# value1 = 'Franklin'
# setPy.add(value1)
# print(setPy)
# print('Тип данных = ',type(setPy))
# print('Количество значений: ',len(setPy))

party_goers = {'Артем','Светлана','Катерина',"Ян"}
print('Тип данных: ', type(party_goers))
print('Первое множество: ', party_goers)

print('\nИдет ли Ян в спортзал ?', 'Ян' in party_goers)
print('Идет ли Мария в парикмахерскую ? ', 'Мария'in party_goers)
fromName = 'Ян' in party_goers
print('Через переменную:Идет ли Ян в спортзал ? ', fromName)

students ={'Артем', 'Оксана','Лилия','Ян'}
print('Второе множество: ', students)
commons = party_goers.intersection(students)
print('\nСодержатся одни и те же в разных множествах = ', commons)

# Преобразование множества в список.
party_students = list(commons)
print('Студенты в библиотеке: ', party_students)
print('Первый библиотечный студент: ', party_students[0])

easy_student = "Альберт"
party_students.append(easy_student)
print('Добавили Альберта ? ', party_students)
print('По индексу 2 = ', party_students[2])