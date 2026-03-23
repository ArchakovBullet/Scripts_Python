from tkinter import*

window = Tk()
window.title ('Пример кнопки.')

btn_end = Button(window, text = 'Закрыть', command = exit)


def tog():
    if window.cget('bg') == 'magenta':
        window.configure(bg='lightgray')
    else:
        window.configure(bg='magenta')
    
btn_tog = Button(window, text='Переключить', command=tog)

btn_tog.pack(padx = 120, pady = 20)
btn_end.pack(padx=120, pady=20)

window.mainloop()