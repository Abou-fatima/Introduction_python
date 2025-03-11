from tkinter import *
def action():
    N = int(entryNombre.get())
    lbDiviseur['text'] = "Diviseurs de N : "
    for i in range(1, N+1):
        if N % i == 0:
            lbDiviseur["text"] = lbDiviseur["text"] + " " + str(i)+" "


fen = Tk()
fen.title("Mon premier TP en Python")
fen.geometry("400x175")
libNombre = Label(fen, text="Entrer la valeur de N : ")
libNombre.place(x=10, y=20)
entryNombre = Entry(fen)
entryNombre.place(x=200, y=20)
lbDiviseur = Label(fen, text="Les diviseurs sont : ")
lbDiviseur.place(x=10, y=50)

btValidate = Button(fen, text="Valider l'operation", command=action)
btValidate.place(x=200, y=90)

fen.mainloop()