# Переопределение методов.
class Person:
    '''''Базовый класс Person, определяющий особенности человека.'''

    def __init__(self, name):
        self.name = name
    
    def speak(self, msg ='Вызов базового класса'):
        print(self.name, msg)
        