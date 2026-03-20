from Person import*

class Man(Person):
    '''Производный класс, определяющий особенности класса Man'''

    def speak(self, msg):
        '''Метод speak класса Man'''
        print(self.name, ':\n\tHello\n', msg)