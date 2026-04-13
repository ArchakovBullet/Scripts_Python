''''''' Первая программа "Шарик за курсором, стр. 36 книги." '''

import pygame as pg, sys
import os

pg.init()


# Перемещаем окно на второй монитор (если он есть)
# Расположение окна при запуске программы на втором мониторе (справа)
# Эта переменная ниже должна быть создана до pg.display.set_mode((800, 600))
os.environ['SDL_VIDEO_WINDOW_POS'] = " 2480,240 "

# Размер окошка:
screen = pg.display.set_mode((800, 600))
# screen = pg.display.set_mode((1000, 300))

# надпись на окошке слева вверху:
pg.display.set_caption('Лети к курсору')

#  начальные координаты объекта(шарика) в окошке при запуске.
x,y= 400,300
size = 50 #размер шарика. Можно например 200 бахнуть.
color = (255,0,0) # цвет красный. Если зеленый то: (0, 255, 0)
# color = (0,255,0)   # зеленый то: (0, 255, 0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()

    # screen.fill((0,0,0))  

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]: 
        screen.fill((0,0,255))

    if keys[pg.K_KP_PLUS]: 
        size = 100
    if keys[pg.K_KP_MINUS]: 
        size = 10
       

    pg.draw.circle(screen, color, (x, y), size)
    pg.display.flip()
    pg.time.delay(10)
