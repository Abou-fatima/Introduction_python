import tkinter as tk

app = tk.Tk()
app.geometry("500x400")
app.title("Les menu bar")

menubar = tk.Menu(app)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Ouvrir")
filemenu.add_command(label="Enregistrer")
filemenu.add_command(label="Quitter")

eleves = tk.Menu(menubar)
eleves.add_command(label="Alpha ousmane Bah")
eleves.add_command(label="Oumou Barry")
eleves.add_cascade(label="Abdoulaye")

matieres = tk.Menu(menubar)
matieres.add_command(label="Python")
matieres.add_command(label="JavaScript")
matieres.add_cascade(label="Node Js")

niveaux = tk.Menu(menubar)
niveaux.add_command(label="P16")
niveaux.add_command(label="P17")
niveaux.add_cascade(label="P18")

menubar.add_cascade(label="Fichier", menu=filemenu)
menubar.add_cascade(label="Eleves", menu=eleves)
menubar.add_cascade(label="Niveau", menu=niveaux)
menubar.add_cascade(label="Matieres",menu=matieres)

app.config(menu=menubar)

app.mainloop()