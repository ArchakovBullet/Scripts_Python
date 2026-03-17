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