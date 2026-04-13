# Шаг № 1  Диагностическая программа для определения мониторов
import pygame as pg
import sys

pg.init()

# Получаем информацию о всех мониторах
monitors = pg.display.get_desktop_sizes()
print("=" * 50)
print("ИНФОРМАЦИЯ О ВАШИХ МОНИТОРАХ:")
print("=" * 50)

for i, size in enumerate(monitors):
    print(f"Монитор {i}: {size[0]} x {size[1]} пикселей")
    
# Определяем расположение мониторов (для Windows)
try:
    import ctypes
    user32 = ctypes.windll.user32
    
    # Получаем координаты всех мониторов
    class MONITORINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("rcMonitor", ctypes.c_long * 4),
                    ("rcWork", ctypes.c_long * 4),
                    ("dwFlags", ctypes.c_uint)]
    
    monitors_info = []
    def monitor_enum_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
        monitor_info = MONITORINFO()
        monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
        user32.GetMonitorInfoW(hMonitor, ctypes.byref(monitor_info))
        monitors_info.append((
            monitor_info.rcMonitor[0],  # left
            monitor_info.rcMonitor[1],  # top
            monitor_info.rcMonitor[2],  # right
            monitor_info.rcMonitor[3]   # bottom
        ))
        return True
    
    # Перечисляем все мониторы
    enum_proc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, 
                                   ctypes.POINTER(ctypes.c_long), ctypes.c_void_p)
    user32.EnumDisplayMonitors(None, None, enum_proc(monitor_enum_proc), 0)
    
    print("\nРАСПОЛОЖЕНИЕ МОНИТОРОВ:")
    for i, info in enumerate(monitors_info):
        left, top, right, bottom = info
        width = right - left
        height = bottom - top
        print(f"Монитор {i}: позиция ({left}, {top}) - размер {width}x{height}")
        
except:
    print("\nНе удалось определить расположение (это нормально для Linux/Mac)")
    print("Предполагаем, что мониторы расположены горизонтально")

pg.quit()

print("\n" + "=" * 50)
print("Теперь запустите основную программу")
input("Нажмите Enter для выхода...")