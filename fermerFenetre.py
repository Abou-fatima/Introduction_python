
from tkinter import *


def fermer():
    fen.quit()

fen = Tk()

fen.geometry("500x250")

#button = Button(fen, text="Fermer la fenêtre! ", width=25, command=quit)
button = Button(fen, text="Fermer la fenêtre! ", width=25, command=fermer)

button.place(x = 150 , y = 100)


fen.mainloop()