from Person import*

class Man(Person):
    '''Производный класс, определяющий особенности класса Man'''

    def speak(self, msg):
        print(self.name, ':\n\tHello', msg)