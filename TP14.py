from tkinter import *
from Centrer import centrer_fenetre
import sqlite3
connection = sqlite3.connect('mydatabase.db')

def validation():
    ResultatNom = nom.get()
    ResultatPrenom = prenom.get()
    ResultatAge = age.get()

    insertion = "insert into students (name, email, age) values(?, ?, ?)"




fen = Tk()
centrer_fenetre(fen, 500, 400)
fen['background'] = 'blue'

label1 = Label(fen, text="Nom : ")
label1.place(x=10, y=50)
nom = Entry(fen, width=25)
nom.place(x=70, y=50)
label2 = Label(fen, text="Email : ")
label2.place(x=10, y=100)
prenom = Entry(fen, width=25)
prenom.place(x=70, y=100)
label3 = Label(fen, text="Age : ")
label3.place(x=10, y=150)
age = Entry(fen, width=25)
age.place(x=70, y=150)

validate = Button(fen, text="Valider l'opération !", command=validation)
validate.place(x=170, y=200)
validate['background'] = 'green'

fen.mainloop()