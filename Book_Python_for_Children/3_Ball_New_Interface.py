'''''''Новый интерфейс старого кода(стр.50) '''''''

import pygame as pg, sys
import os

pg.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '2480, 240'
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Взлетаем к курсору')

print('\n' +'#' * 50)
print('Для выхода из игры нажмите Escape\nлибо нажмите крестик.\n')
print('\n' +'#' * 50)

# Небесно-голубой
sky_blue = (135, 206, 235)

# Лимонный
lemon = (255, 255, 0)

# Вишневый
cherry = (222, 49, 99)

# Морская волна
sea_green = (46, 139, 87)

# Шоколадный
chocolate = (210, 105, 30)

red_color = (255, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)
orange_color = (255, 165, 0)
purple_color = (128, 0, 128)
black = (0,0,0)

x,y = 400,300
size = 60
color = cherry

font = pg.font.SysFont('Arial', 24)

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x,y = pg.mouse.get_pos()
            pg.draw.circle(screen, color, (x,y), size)

    keys = pg.key.get_pressed()
    mods = pg.key.get_mods()

    if keys[pg.K_1]: color = red_color
    if keys[pg.K_2]: color = lemon
    if keys[pg.K_3]: color = green_color

    if keys[pg.K_SPACE]: screen.fill(sky_blue)

    if 15 < size < 100:
        if keys[pg.K_KP_MINUS]: size -= 1
        elif keys[pg.K_KP_PLUS]: size += 1
    else: size = 60

    pg.draw.rect(screen, (50,50,50), (0,550,800, 50))
    pg.draw.circle(screen,color, (50,575), 15)
    pg.draw.circle(screen,(200, 200,200), (50, 575), 15, 1 )
    size_text = font.render(f'Размер: {size} ', True, (255,255,255))
    screen.blit(size_text, (80,560))

    pg.display.flip()
    clock.tick(60)






