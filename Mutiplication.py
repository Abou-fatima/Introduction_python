from tkinter import *
from tkinter import ttk
from Centrer import centrer_fenetre  # Assurez-vous que ce module est bien présent


def action(event):
    Resultat = listCombo.get()
    _, _, chiffre = Resultat.partition(":")  # Récupère ce qui est après ":"
    chiffre = chiffre.strip()  # Supprime les espaces

    try:
        N = int(chiffre)  # Convertir en entier
        texte_resultat = f"Table de {N} :\n"

        # Générer la table de multiplication
        for i in range(1, 11):
            texte_resultat += f"{N} × {i} = {N * i}\n"

        label_resultat.config(text=texte_resultat)  # Met à jour l'affichage du Label

    except ValueError:
        label_resultat.config(text="Erreur : Valeur non valide")


# Création de la fenêtre principale
fen = Tk()
centrer_fenetre(fen, 500, 400)  # Fonction pour centrer la fenêtre
fen['background'] = 'blue'
fen.title("Tables de Multiplication")

# Label pour afficher le titre
label = Label(fen, text="Sélectionnez une table :", font=("Arial", 12), bg="blue", fg="white")
label.place(x=15, y=20)

# Liste des tables de multiplication
list_tables = [
    "Table de multiplication de : 1",
    "Table de multiplication de : 2",
    "Table de multiplication de : 3",
    "Table de multiplication de : 4",
    "Table de multiplication de : 5",
    "Table de multiplication de : 6",
    "Table de multiplication de : 7",
    "Table de multiplication de : 8",
    "Table de multiplication de : 9",
    "Table de multiplication de : 10"
]

# Création du Combobox pour la sélection
listCombo = ttk.Combobox(fen, values=list_tables, width=30, state="readonly")
listCombo.current(0)  # Sélectionne par défaut la table 1
listCombo.place(x=15, y=50)
listCombo.bind('<<ComboboxSelected>>', action)  # Lier la sélection à la fonction action

# Label pour afficher la table de multiplication
label_resultat = Label(fen, text="", font=("Arial", 12), bg="blue", fg="white", justify=LEFT)
label_resultat.place(x=15, y=100)

# Lancement de la fenêtre Tkinter
fen.mainloop()
