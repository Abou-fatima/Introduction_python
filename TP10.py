from tkinter import *

def action(event):
    s = int(sp.get())
    fenetre.geometry('{}x{}'.format(400+s*25, 250+s*25))

fenetre = Tk()
fenetre.geometry('400x250')
fenetre.title('Redimension de la fênetre')

sp = Spinbox(fenetre, from_=1 , to=8)
sp.pack()
sp.bind('<Button-1>', action)

resize = Label(fenetre, text="Redimensionez")
resize.pack()


fenetre.mainloop()