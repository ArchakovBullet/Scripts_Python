from Book_MacGrat.Person_MAN_HOMBRE.Man import*
from Book_MacGrat.Person_MAN_HOMBRE.Hombre import*

guy1 = Man('Ричард')
guy2 = Hombre('Рикардо')

guy1.speak('It\'s a beautiful evening.\n ')
guy2.speak('Es una tarde hermosa.\n')

Person.speak(guy1)
Person.speak(guy2)

