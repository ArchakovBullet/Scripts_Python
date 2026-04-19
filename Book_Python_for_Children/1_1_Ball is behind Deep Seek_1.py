import pygame as pg
import sys
import os

def get_monitor_layout():
    """Определяет расположение и размеры всех мониторов"""
    monitors = pg.display.get_desktop_sizes()
    
    # Пытаемся определить точные координаты мониторов (Windows)
    try:
        import ctypes
        
        user32 = ctypes.windll.user32
        monitors_positions = []
        
        class MONITORINFO(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_uint),
                        ("rcMonitor", ctypes.c_long * 4),
                        ("rcWork", ctypes.c_long * 4),
                        ("dwFlags", ctypes.c_uint)]
        
        def monitor_enum_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
            monitor_info = MONITORINFO()
            monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
            user32.GetMonitorInfoW(hMonitor, ctypes.byref(monitor_info))
            monitors_positions.append((
                monitor_info.rcMonitor[0],  # left
                monitor_info.rcMonitor[1],  # top
                monitor_info.rcMonitor[2],  # right
                monitor_info.rcMonitor[3]   # bottom
            ))
            return True
        
        enum_proc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p,
                                       ctypes.POINTER(ctypes.c_long), ctypes.c_void_p)
        user32.EnumDisplayMonitors(None, None, enum_proc(monitor_enum_proc), 0)
        
        # Формируем список мониторов с координатами
        monitors_with_pos = []
        for i, pos in enumerate(monitors_positions):
            left, top, right, bottom = pos
            width = right - left
            height = bottom - top
            monitors_with_pos.append({
                'index': i,
                'x': left,
                'y': top,
                'width': width,
                'height': height,
                'size': (width, height)
            })
        
        return monitors_with_pos
    
    except:
        # Если не удалось определить (Linux/Mac), предполагаем горизонтальное расположение
        print("Не удалось определить точное расположение мониторов")
        print("Предполагаем горизонтальное расположение")
        
        monitors_with_pos = []
        current_x = 0
        for i, size in enumerate(monitors):
            monitors_with_pos.append({
                'index': i,
                'x': current_x,
                'y': 0,
                'width': size[0],
                'height': size[1],
                'size': size
            })
            current_x += size[0]
        
        return monitors_with_pos

def center_window_on_monitor(monitor_index, window_width=800, window_height=600):
    """Устанавливает позицию окна по центру указанного монитора"""
    monitors = get_monitor_layout()
    
    if monitor_index >= len(monitors):
        print(f"Монитор {monitor_index} не найден. Использую монитор 0")
        monitor_index = 0
    
    monitor = monitors[monitor_index]
    
    # Вычисляем координаты для центрирования окна
    center_x = monitor['x'] + (monitor['width'] - window_width) // 2
    center_y = monitor['y'] + (monitor['height'] - window_height) // 2
    
    # Устанавливаем переменную окружения для позиции окна
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{center_x},{center_y}"
    
    print(f"Окно будет открыто на мониторе {monitor_index}")
    print(f"Размер монитора: {monitor['width']}x{monitor['height']}")
    print(f"Позиция окна: ({center_x}, {center_y})")
    
    return center_x, center_y

def main():
    pg.init()
    
    # Параметры окна
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    
    # Выводим информацию о мониторах
    print("\n" + "=" * 50)
    print("НАЙДЕННЫЕ МОНИТОРЫ:")
    print("=" * 50)
    
    monitors = get_monitor_layout()
    for mon in monitors:
        print(f"Монитор {mon['index']}: {mon['width']}x{mon['height']} "
              f"в позиции ({mon['x']}, {mon['y']})")
    
    print("=" * 50)
    
    # Выбираем второй монитор (индекс 1)
    # Если его нет, используем первый
    target_monitor = 1 if len(monitors) > 1 else 0
    
    if len(monitors) <= 1:
        print("\nВнимание: Обнаружен только один монитор!")
        print("Окно будет открыто на основном мониторе\n")
    
    # Центрируем окно на выбранном мониторе
    center_window_on_monitor(target_monitor, WINDOW_WIDTH, WINDOW_HEIGHT)
    
    # Создаем окно
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Лети к курсору')
    
    # Начальные параметры
    x, y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
    size = 50
    color = (255, 0, 0)
    
    print("\nУправление:")
    print("- Клик мышкой - шарик летит к курсору")
    print("- Пробел - заливка экрана синим цветом")
    print("- NumPad + - увеличить шарик до 100")
    print("- NumPad - - уменьшить шарик до 10")
    print("- Закройте окно для выхода\n")
    

    clock = pg.time.Clock()  # создаем часы(вместо  pg.time.delay(10)) 

    # Основной цикл
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:  # Выход при нажатии Escape.
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
        
        # Обработка нажатий клавиш
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            screen.fill((0, 0, 255))
        else:
            # Каждый кадр очищаем экран (если не зажат пробел)
            screen.fill((255, 255, 255))
        
        if keys[pg.K_KP_PLUS]:
            size = 100
        if keys[pg.K_KP_MINUS]:
            size = 10
        
        # Рисуем шарик
        pg.draw.circle(screen, color, (x, y), size)
        pg.display.flip()
        # pg.time.delay(10)
        clock.tick(60)

if __name__ == "__main__":
    main()