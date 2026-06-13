import pygame as pg 
import sys
import os

# Инициализация Pygame и настройка окна
def init_pygame():
    pg.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '2480, 240'
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption('Взлетаем к курсору')
    return screen

# Вывод инструкций в консоль
def print_instructions():
    print('\n' + '#' * 50)
    print('Для выхода из игры нажмите Escape\nлибо нажмите крестик.\nSpace для очистки от следов')
    print('\n1,2,3 - выбор цвета\n')
    print('Левая кнопка мыши - кисть Круг\nПравая кнопка мыши - кисть Квадрат\n"+"NumPad "-" - увеличение/уменьшение размера')
    print('r - красный цвет шарика\ng - зеленый цвет шарика\nb - синий цвет шарика')
    print('\n' + '#' * 50)

# Определение цветов
def define_colors():
    colors = {
        'sky_blue': (135, 206, 235),
        'lemon': (255, 255, 0),
        'cherry': (222, 49, 99),
        'sea_green': (46, 139, 87),
        'chocolate': (210, 105, 30),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'orange': (255, 165, 0),
        'purple': (128, 0, 128),
        'black': (0, 0, 0),
    }
    return colors

# Обработка событий выхода
def handle_exit_events(event):
    if event.type == pg.QUIT:
        return True
    elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
        return True
    return False

# Обработка кликов мыши для рисования
def handle_mouse_click(event, screen, color, size):
    if event.type == pg.MOUSEBUTTONDOWN:
        x, y = pg.mouse.get_pos()
        
        if event.button == 1:  # левая кнопка мыши - круг
            pg.draw.circle(screen, color, (x, y), size)
        elif event.button == 3:  # правая кнопка мыши - квадрат
            rect = pg.Rect(x - size // 2, y - size // 2, size, size)
            pg.draw.rect(screen, color, rect)

# Обработка изменения цвета через клавиши
def handle_color_change(keys, colors):
    if keys[pg.K_1] or keys[pg.K_r]:
        return colors['red']
    elif keys[pg.K_2]:
        return colors['lemon']
    elif keys[pg.K_3] or keys[pg.K_g]:
        return colors['green']
    elif keys[pg.K_b]:
        return colors['blue']
    # Возвращаем цвет по умолчанию, если не нажаты клавиши цвета
    return colors['cherry']

# Обработка изменения размера
def handle_size_change(keys, current_size):
    if keys[pg.K_KP_MINUS] and current_size > 10:
        current_size -= 1
    if keys[pg.K_KP_PLUS] and current_size < 60:
        current_size += 1
    return current_size

# Отрисовка интерфейса (панель внизу)
def draw_interface(screen, color, size, font):
    # Панель внизу
    pg.draw.rect(screen, (50, 50, 50), (0, 550, 800, 50))
    
    # Отображение текущего цвета
    pg.draw.circle(screen, color, (50, 575), 15)
    pg.draw.circle(screen, (200, 200, 200), (50, 575), 15, 1)
    
    # Отображение текущего размера
    size_text = font.render(f'Размер: {size}', True, (255, 255, 0))
    screen.blit(size_text, (80, 560))

# Основная функция игры
def main():
    screen = init_pygame()
    print_instructions()
    colors = define_colors()
    
    # Начальные значения
    size = 50
    color = colors['cherry']
    font = pg.font.SysFont('Arial', 24)
    clock = pg.time.Clock()
    
    while True:
        # Обработка событий
        for event in pg.event.get():
            if handle_exit_events(event):
                pg.quit()
                sys.exit()
            
            handle_mouse_click(event, screen, color, size)
        
        # Обработка нажатых клавиш
        keys = pg.key.get_pressed()
        
        # Очистка экрана
        if keys[pg.K_SPACE]:
            screen.fill(colors['black'])
        
        # Изменение цвета
        color = handle_color_change(keys, colors)
        
        # Изменение размера
        size = handle_size_change(keys, size)
        
        # Отрисовка интерфейса
        draw_interface(screen, color, size, font)
        
        # Обновление экрана
        pg.display.flip()
        clock.tick(60)

# Запуск игры
if __name__ == "__main__":
    main()