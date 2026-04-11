''''''' Первая программа "Шарик за курсором, стр. 36 книги." '''

import pygame as pg, sys

pg.init()

# Размер окошка:
screen = pg.display.set_mode((800, 600))

# надпись на окошке слева вверху:
pg.display.set_caption('Лети к курсору')

# координаты объекта(шарика) в окошке.
x,y=400,300

size = 60 #размер шарика. Можно например 200 бахнуть.
# color = (255,0,0) # цвет красный. Если зеленый то: (0, 255, 0)
color = (0,255,0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
    screen.fill((0,0,0))
    pg.draw.circle(screen, color, (x, y), size)
    pg.display.flip()
    pg.time.delay(10)
