from tkinter import*
import tkinter.messagebox as box

window = Tk()
window.title('Пример окна сообщения')

def dialog():
    var = box.askyesno('Окно сообщения', 'Обработать ?')
    if var == 1:
        box.showinfo('Окно Да', 'Обработака....')
    else:
        box.showwarning('Окно Нет', 'Отмена.....')

btn = Button(window, text='Клик', command= dialog)

btn.pack(padx= 120, pady= 50)

window.mainloop()
