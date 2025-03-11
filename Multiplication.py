from tkinter import *
def action1(event):
    button['background'] = 'green'
def action2(event):
    button['background'] = 'white'

def resultat():
    nombre1 = int(input1.get())
    nombre2 = int(input2.get())

    reponse = nombre1 * nombre2
    label3['text'] = reponse

def reset():
    label3['text'] = " "
def reset1(event):
    button2['background'] = 'white'

def reset2(event):
    button2['background'] = 'red'




fen = Tk()
fen.geometry('500x250')
fen.title('Multiplication')
fen['background'] = 'blue'

label = Label(fen, text="Entrer la premiere valeur", padx=10, pady=2)
label.place(x=10, y=50)

input1 = Entry(fen, width=35)
input1.place(x=200, y=50)

label1 = Label(fen, text="Entrer la deuxieme valeur", padx=10, pady=2)
label1.place(x=10, y=110)

input2 = Entry(fen, width=35)
input2.place(x=200, y=110)

button = Button(fen, text="Valider !", width=10, command=resultat)
button.place(x=390, y=180)
button.bind('<Enter>', action1)
button.bind('<Leave>', action2)

button2 = Button(fen, text="Reset !", width=10, command=reset)
button2.place(x=300, y=180)
button2.bind('<Enter>', reset2)
button2.bind('<Leave>', reset1)


label2 = Label(fen, text="Le produit de ces deux est : ")
label2.place(x=10, y=200)

label3 = Label(fen, text=" ")
label3.place(x=180, y=200)

fen.mainloop()