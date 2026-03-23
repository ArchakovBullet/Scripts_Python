# Сбор входных данных
from tkinter import*
import tkinter.messagebox as box

window = Tk()
window.title('Пример окна ввода')

frame = Frame(window)
entry = Entry(frame)

def dialog():
    box.showinfo('Приветствие', 'Добро пожаловать  ' + entry.get())

btn = Button(frame, text='Введите имя  ', command= dialog)

btn.pack(side=RIGHT, padx= 5)
entry.pack(side=LEFT)
frame.pack(padx=20, pady=20)

window.mainloop()