from tkinter import *

def action(event):
    Recu = int(input1.get())
    recu2 = Recu*2
    input2.delete(0,END)
    input2.insert(0,recu2)



fen = Tk()

fen.geometry("450x250")
fen.title("Multiplication")




label = Label(fen, text="Donnez un nombre ici : ")
label.place(x = 70, y= 70)

input1 = Entry(fen, width=35)
input1.bind('<Return>', action)
input1.place(x=210, y=70)


label = Label(fen, text="Le double de ce nombre est: ")
label.place(x = 70, y= 140)

input2 = Entry(fen, width=35)
input2.place(x=230, y=140)









fen.mainloop()