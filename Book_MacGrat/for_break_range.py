for i in range(1,4):
    for j in range(1, 4):
        if i == 2 and j == 1:
            print('Прервать внутренний цикл,когда i=2, j = 1')
            break
            # continue
        print('Работа i= ', i, 'j= ', j)

