from tkinter import *
def action():
    label['text'] = "Salut à tous les Developpeurs !"
def reset():
    label['text']=" "


fen = Tk()

fen.geometry("600x250")
fen.title("Mon TP4 en Python")

buttton = Button(fen, text="Commande", width=15, command=action)
buttton.place(x=250, y=100)

buttton = Button(fen, text="Reset", width=10, command=reset)
buttton.place(x=400, y=100)

label = Label(fen)
label.place(x=250, y=150)



fen.mainloop()