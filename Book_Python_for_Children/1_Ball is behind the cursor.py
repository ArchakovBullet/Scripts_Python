''''''' Первая программа "Шарик за курсором, стр. 36 книги." '''

import pygame as pg, sys
import os

pg.init()


# Перемещаем окно на второй монитор (если он есть)
# Расположение окна при запуске программы на втором мониторе (справа)
# Эта переменная ниже должна быть создана до pg.display.set_mode( )
os.environ['SDL_VIDEO_WINDOW_POS'] = " 2480,240 "

# Размер окошка:
screen = pg.display.set_mode((800, 600))

# Если есть желание открыть монитор в полноэкранном режиме,
# но для выхода из программы нужно сделать обработку.Ниже смотри: Выход при нажатии на Escape.
# screen = pg.display.set_mode((0, 0), pg.FULLSCREEN, display=1)

# надпись на окошке слева вверху:
pg.display.set_caption('Лети к курсору')

print("\n" + "#" * 50)
print("#" * 50 + '\n')
print("Для выхода из игры нажмите Escape.")
print('\n' + "#" * 50)
print("#" * 50)

#  начальные координаты объекта(шарика) в окошке при запуске.
x,y= 400,300
size = 50 #размер шарика. Можно например 200 бахнуть.
color = (255,0,0) # цвет красный. Если зеленый то: (0, 255, 0)
# color = (0,255,0)   # зеленый то: (0, 255, 0)


clock = pg.time.Clock()  # альтернатива  pg.time.delay(10) 

# По сути, это ДВИЖОК ПРОГРАММЫ.
while True: # Бесконечный игровой цикл. 
    for event in pg.event.get():  # Получаем накопившиеся события.
        if event.type == pg.QUIT: # Нажал на крестик ?
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN: # Обрабатываем нажатие клавиш
            if event.key == pg.K_ESCAPE: # ESCAPE
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN: # Нажал кнопку мыши ?
            x,y = pg.mouse.get_pos()  # Получаем координаты мыши.

    screen.fill((0,0,0))   # Закрашивает экран черным цветом

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]: # Если нажал на пробел,
        screen.fill((0,0,255))  # то, окно станет синим.

    if keys[pg.K_KP_PLUS]: 
        size = 100
    if keys[pg.K_KP_MINUS]: 
        size = 10
       

    pg.draw.circle(screen, color, (x, y), size)
    pg.display.flip()
    # pg.time.delay(10)  # задержка на 10 милисекунд, чтобы не перегревался процессор. Этой строке есть альтернатива.
    clock.tick(60)
