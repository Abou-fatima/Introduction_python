from tkinter import  *


def action():
    N = int(entrer.get())
    N2 = 2*N
    entrer2.delete(0, END)
    entrer2.insert(0, N2)


fene = Tk()
fene.geometry("500x300")
fene.title("Mon deuxieme TP en Python")


label1 = Label(fene, text="Entrer la valeur de N : ")
label1.place(x = 50, y = 50)
entrer = Entry(fene)
entrer.place(x = 200 , y = 50)

label2 = Label(fene, text="Le double de N est : ")
label2.place(x = 50, y = 100)
entrer2 = Entry(fene)
entrer2.place(x = 200 , y = 100)

button = Button(fene ,text="Valider l'operation", command=action)
button.place(x = 200, y = 150)
fene.mainloop()