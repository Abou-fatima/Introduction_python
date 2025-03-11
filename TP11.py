from tkinter import *
from tkinter import ttk
from Centrer import centrer_fenetre
from math import gcd

def action(event):
    fen['background'] = 'green'

def action1(event):
    fen['background'] = 'blue'




def resultat(event):
    selection = menuDeroulant.get()
    valeurM = int(entrer1.get())
    valeurN = int(entrer2.get())

    pgcd = gcd(valeurM, valeurN)
    ppcm = int((valeurM*valeurN)/pgcd)

    if selection == "PGCD":
        labelResultat['text'] = 'PGCD = ' + str(pgcd)
    else:
        labelResultat['text'] = "PPCM = " + str(ppcm)


fen = Tk()
centrer_fenetre(fen, 500, 300)
fen.title('PGCD et PPCM')
fen['background'] = 'blue'
fen.bind('<Enter>', action)
fen.bind('<Leave>',action1)


label1 = Label(fen, text="Valeur de m")
label1.place(x=10, y=50)
entrer1 = Entry(fen)
entrer1.place(x=100, y=50)

label2 = Label(fen, text="Valeur de n")
label2.place(x=10, y=90)
entrer2 = Entry(fen)
entrer2.place(x=100, y=90)

menuDeroulant = ttk.Combobox(fen, values=['PGCD', 'PPCM'], width=17)
label3 = Label(fen, text="Choisir ")
label3.place(x=10, y=130)
menuDeroulant.place(x=100,y=130)
menuDeroulant.bind("<<ComboboxSelected>>", resultat)

label4 = Label(fen, text="Le resultat est : ")
label4.place(x=10, y=170)

labelResultat = Label(fen, text="")
labelResultat.place(x=100, y=170)
fen.mainloop()