from tkinter import *

def action():
    message = input.get()
    label["text"] = "Salut " + message

def reset():
    label['text'] = " "

def action1(event):
    button2['background']= 'white'
def action2(event):
    button2['background']= 'red'
def action3(event):
    button1['background']= 'green'
def action4(event):
    button1['background']= 'white'

fen = Tk()


fen.geometry("400x250")
fen.title('Mon TP6 en Python')

label = Label(fen, text="Entrer votre nom : ")
label.place(x=50, y=70)

input = Entry(fen, textvariable='Votre nom')
input.place(x=170, y = 70)

button1 = Button(fen, text="Valider", width=10, command=action)
button1.place(x = 180, y=110)
button1.bind('<Enter>', action3)
button1.bind('<Leave>', action4)



button2 = Button(fen, text="Reset", width=10, command=reset)
button2.place(x = 280, y=110)
button2.bind('<Leave>', action1)
button2.bind('<Enter>', action2)

label = Label(fen, text="")
label.place(x=120, y=150)






fen.mainloop()