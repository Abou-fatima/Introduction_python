from tkinter import *

def action1(event):
    fen['background'] ='yellow'


def action2(event):
    fen['background'] = 'black'


fen = Tk()

fen.geometry('400x400')
fen.title('Survoler avec la sourris')
fen.bind('<Enter>', action1)
fen.bind('<Leave>', action2)
fen.colormapwindows()
fen.mainloop()