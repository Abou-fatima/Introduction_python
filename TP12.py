from tkinter import *
from Centrer import centrer_fenetre

def Resultat():
    try:
        PremiereValeur = float(entrer1.get())  # Convertir en float
        DeuxiemeValeur = float(entrer2.get())  # Convertir en float

        Somme = PremiereValeur + DeuxiemeValeur
        Difference = PremiereValeur - DeuxiemeValeur
        Produit = PremiereValeur * DeuxiemeValeur
        Quotient = PremiereValeur / DeuxiemeValeur

        labelSomme['text'] = 'S = ' + str(Somme)

        if PremiereValeur > DeuxiemeValeur:
            labelDifference['text'] = 'D = ' + str(Difference)
        else:
            labelDifference['text'] = 'La première valeur doit être plus grande'

        labelProduit['text'] = 'P = ' + str(Produit)

        if DeuxiemeValeur == 0:
            labelQuotient['text'] = 'Le deuxième nombre doit être différent de zéro'
        else:
            labelQuotient['text'] = 'Q = ' + str(Quotient)

    except ValueError:
        labelSomme['text'] = "Entrée invalide"
        labelDifference['text'] = "Entrée invalide"
        labelProduit['text'] = "Entrée invalide"
        labelQuotient['text'] = "Entrée invalide"
    except ZeroDivisionError:
        labelQuotient['text'] = 'Division par zéro est impossible'

fen = Tk()
centrer_fenetre(fen, 500, 400)
fen['background'] = 'blue'
fen.title('Operation Sur les nombres')

label1 = Label(fen, text="Premiere valeur : ")
label1.place(x=10, y=50)
entrer1 = Entry(fen)
entrer1.place(x=200, y=50)
label2 = Label(fen, text="Deuxieme valeur : ")
label2.place(x=10, y=100)
entrer2 = Entry(fen)
entrer2.place(x=200, y=100)
label3 = Label(fen, text="La somme est : ")
label3.place(x=10, y=150)
labelSomme = Label(fen, text="")
labelSomme.place(x=200, y=150)
label4 = Label(fen, text="La difference est : ")
label4.place(x=10, y=200)
labelDifference = Label(fen, text="")
labelDifference.place(x=200, y=200)
label5 = Label(fen, text="La produit est : ")
label5.place(x=10, y=250)
labelProduit = Label(fen, text="")
labelProduit.place(x=200, y=250)
label3 = Label(fen, text="Le quotient est : ")
label3.place(x=10, y=300)
labelQuotient = Label(fen, text="")
labelQuotient.place(x=200, y=300)

Validation = Button(fen, text="Valider !", command=Resultat)
Validation.place(x=390, y=350)
Validation['background'] = 'green'




fen.mainloop()