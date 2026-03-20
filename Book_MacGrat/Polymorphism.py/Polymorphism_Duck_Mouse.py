from Duck import*
from Mouse import*

def describe (object):
    object.talk()
    object.coat()

dolly = Duck()
monty = Mouse()

describe(dolly)
describe(monty)

dolly.talk()
dolly.coat()
monty.talk()
monty.coat()
