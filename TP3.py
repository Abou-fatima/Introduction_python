from tkinter import *


fenetre = Tk()

fenetre.geometry("600x400")

button1 = Button(fenetre, text="Button1" , width=30)

button2 = Button(fenetre, text="Button2", width=30)

button3 = Button(fenetre, text="Button3", width=30)

button4 = Button(fenetre, text="Button4", width=30)

button1.grid(row = 0, column =0,padx=13, pady=13)
button2.grid(row = 0, column =1 ,padx=13, pady=13)
button3.grid(row = 1, column =0,padx=13, pady=13)
button4.grid(row = 1, column =1,padx=13, pady=13)
fenetre.mainloop()