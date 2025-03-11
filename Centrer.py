import tkinter as tk


def centrer_fenetre(fenetre, largeur=400, hauteur=300):
    # Obtenir la taille de l'écran
    largeur_ecran = fenetre.winfo_screenwidth()
    hauteur_ecran = fenetre.winfo_screenheight()

    # Calculer les coordonnées pour centrer la fenêtre
    x = (largeur_ecran - largeur) // 2
    y = (hauteur_ecran - hauteur) // 2

    # Définir la géométrie de la fenêtre
    fenetre.geometry(f"{largeur}x{hauteur}+{x}+{y}")
