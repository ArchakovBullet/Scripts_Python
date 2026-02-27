# Условная конструкция if else
language = 'English'
if  language == 'English':
    print("Да сэр.")
else:
    print('Нееет сэр.')

# elif
# Если необходимо ввести несколько альтернативных условий, 
# то можно использовать дополнительные блоки elif, 
# после которого идет блок инструкций.
language = "russian"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")

# При необходимости можно определить несколько блоков elif для разных условий. 
language = "french"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Привет")

#  Конструкция if в свою очередь сама может иметь вложенные конструкции if 
language = 'russian'
dataTime = 'morning'
if language == 'russian':
    print('Norway')
    if dataTime == 'morning':
        print('Здравствуйте')
    else:
        print('Учитесь говорить по русски.')

# Подобным образом можно размещать вложенные конструкции if/elif/else 
# в блоках elif и else:
language = "russian"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")