from Person import*

'''Производный класс, определеяющий особенности класса Hombre'''
class Hombre(Person):

    def speak(self, msg):
        print(self.name, '\n\t\Hola', msg)
