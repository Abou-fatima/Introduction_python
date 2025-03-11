from tkinter import *


fenetre = Tk()

fenetre.geometry("300x150")

button1 = Button(fenetre, text="Button1")
#button1.place(x = 0, y = 0)

button2 = Button(fenetre, text="Button2")
#button2.place(x = 53, y = 0)

button3 = Button(fenetre, text="Button3")
#button3.place(x = 0, y = 26)

button4 = Button(fenetre, text="Button4")
#button4.place(x = 53, y = 26)

# oubien
button1.grid(row = 0, column =0)
button2.grid(row = 0, column =1)
button3.grid(row = 1, column =0)
button4.grid(row = 1, column =1)
fenetre.mainloop()