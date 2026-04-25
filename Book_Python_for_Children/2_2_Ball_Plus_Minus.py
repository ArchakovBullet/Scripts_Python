# В этом примере я буду делать сам ручками, а не копировать код.
''''''' Продолжение легендарно нашумевшей игры "Щарик за курсором" '''''''''

import pygame as pg, sys, os

pg.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = '2480,240' # Какой экран будет использоваться.

screen = pg.display.set_mode((800,600)) #  размер окошка.

# Если есть желание, чтобы экран был во весь экран:
# screen = pg.display.set_mode((0,0), pg.FULLSCREEN, display= 1)

pg.display.set_caption('Полет к курсору')


print('\n' +'#' * 50)
print('Для выхода из игры нажмите Escape\nлибо нажмите крестик.\n')
print('Для очистки от следов левый Ctrl')
print('\n' +'#' * 50)

x,y = 400,300
size = 60
color = (255,0,0)


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

last_printed_state = None # 'alt', 'space', или None

clock = pg.time.Clock()

# Чтобы окошко закрывалось не сразу.
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

    
    # screen.fill((0,0,0))

    keys = pg.key.get_pressed()
    mods = pg.key.get_mods()


    # if mods & pg.KMOD_ALT:
    #     screen.fill(orange_color)
    #     current_state = 'alt'
    # elif keys[pg.K_SPACE]:
    #     screen.fill(blue_color)
    #     current_state = 'space' 
    # else:
    #     screen.fill(black)
    #     current_state = None
        
    # if current_state != last_printed_state:
    #     if current_state == 'alt':
    #         print('Alt зажата')
    #     elif current_state == 'space':
    #         print('Зажат пробел')
    
    #     last_printed_state = current_state


    if mods & pg.KMOD_CTRL: # Очищаем от следов.
        screen.fill(black)

    if keys[pg.K_1]:
        color = chocolate
    elif keys[pg.K_2]:
        color = lemon
    elif keys[pg.K_3]:
        color = purple_color

    control = size > 15 and size < 100
    if control:
        if keys[pg.K_KP_PLUS]:
            size += 1

        elif keys[pg.K_KP_MINUS]:
            size -=1
    else:
        size = 60
        # color = sky_blue



    pg.draw.circle(screen, color, (x,y), size)
    pg.display.flip()
    clock.tick(60)
        



