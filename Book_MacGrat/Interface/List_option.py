# Список опций.

from tkinter import*
import tkinter.messagebox as box

window = Tk()
window.title('Пример окна списка')

frame = Frame(window)

listbox = Listbox(frame)
listbox.insert(1,'HTML in easy steps')
listbox.insert(2, 'CSS in easy steps')
listbox.insert(3, 'JavaScript in easy steps')

def dialog():
    box.showinfo('Selection', 'Your Choice' + \
                 listbox.get(listbox.curselection()))

btn = Button(frame, text='Выберите один вариант', command=dialog)

btn.pack(side=RIGHT, padx= 5)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()