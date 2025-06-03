from tkinter import *
from Centrer import centrer_fenetre

def action(event):
 resultat = input.get()
 label1['text'] = 'Hello : ' + resultat

fen = Tk()
centrer_fenetre(fen, 500, 400)
fen['background'] = 'blue'
label = Label(fen, text="Entrer votre nom ici  : ")
label.place(x=10, y=100)

input = Entry(fen)
input.place(x=200, y=100)
input.bind('<Return>', action)

label1 = Label(fen, text="")
label1.place(x=200, y=200)

fen.mainloop()