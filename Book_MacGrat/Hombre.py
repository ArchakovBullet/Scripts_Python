from Person import*

class Hombre(Person):
    '''Производный класс, определеяющий особенности класса Hombre'''

    def speak(self, msg):
        ''''Метод speak класса Hombre'''
        print(self.name, ':\n\tHola\n', msg)
