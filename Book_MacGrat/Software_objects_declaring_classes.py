# Объявление классов.
# Простой класс:
class Person:
    #  Класс, представляющий человека.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.number = number

    def inroduce(self):
        return f'Привет, меня зовут {self.name}, мне {self.age} лет.'

person = Person('Артем', 33)
print(person.inroduce())

# Класс с свойствами класса и экземпляра:
class Employee:
    # Атрибуты класса (общие для всех экземпляров)
    company = "Tech Corp"
    employee_count =0

    def __init__(self, name, position, salary):
        # Атрибуты экземпляра
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
    
    def get_info(self):
        return f'{self.name} - {self.position}, зарплата: {self.salary}'
    
    @classmethod
    # @classmethod — это декоратор, 
    # который превращает обычный метод в метод класса. 
    # В отличие от обычных методов экземпляра, 
    # метод класса получает первым аргументом не self (экземпляр), а cls (сам класс).
    def get_company_info(cls):
        return f'Компания: {cls.company}, сотрудников: {cls.employee_count}'

# Использование
emp1 = Employee('Иван', 'Разработчик', 150000)
emp2 = Employee('Анна', 'Бухгалтер', 120000)
print(Employee.get_company_info())
print(Employee.get_info(emp1))
print(Employee.get_info(emp2))

