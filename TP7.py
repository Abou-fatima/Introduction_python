from tkinter import *


def action(event):
   name = input.get()
   label1['text'] = "Salut " + name

fen = Tk()

fen.geometry('400x250')
fen.title('Mon TP7 en Python')

label = Label(fen, text="Donnez votre nom : ")
label.place(x = 70, y= 70)

input = Entry(fen)
input.place(x=190, y=70)

input.bind('<Return>', action)

label1 = Label(fen, text="")
label1.place(x=190, y=120)







fen.mainloop()