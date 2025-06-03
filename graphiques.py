# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 16:00:37 2025

@author: abouf
""" 
# import des bubliothèques qui seront utilisés durant le projet
from Centrer import centrer_fenetre
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from datetime import datetime
from PIL import Image as PILImage
import os
# === Chemin du fichier Excel ===
file_path = "C:/TPPYTHON/donnees_crud.xlsx"

sheet_name = "Feuil1"

# === Créer le fichier s'il n'existe pas ===
if not os.path.exists(file_path):
    df_init = pd.DataFrame(columns=["Nom", "Âge", "Ville"])
    df_init.to_excel(file_path, index=False, sheet_name=sheet_name)

# ===Les Fonctions CRUD ===
def charger_données():
    return pd.read_excel(file_path, sheet_name=sheet_name)

def enregistrer_données(df):
    df.to_excel(file_path, index=False, sheet_name=sheet_name)
# Fonction pour inserer les données dans la base de donnée
def inserer_données():
    nom = entry_nom.get().strip()
    age = entry_age.get().strip()
    ville = entry_ville.get().strip()

    if not nom or not age or not ville:
        messagebox.showwarning("Erreur", "Tous les champs sont obligatoires.")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Erreur", "L'âge doit être un nombre.")
        return

    df = charger_données()
    if ((df['Nom'] == nom) & (df['Âge'] == age) & (df['Ville'] == ville)).any():
        messagebox.showinfo("Info", "Cette entrée existe déjà.")
        return

    df = pd.concat([df, pd.DataFrame([[nom, age, ville]], columns=["Nom", "Âge", "Ville"])], ignore_index=True)
    enregistrer_données(df)
    mettreAJour_liste()
    vider_champs()
    messagebox.showinfo("Succès", "Insertion effectuée avec succès.")

def mettreAJour_liste():
    listbox.delete(0, tk.END)
    df = charger_données()
    for i, row in df.iterrows():
        listbox.insert(tk.END, f"{i+1}. {row['Nom']} - {row['Âge']} - {row['Ville']}")
# Fonction pour selectionner 
def selectionner_liste(event):
    try:
        index = listbox.curselection()[0]
        df = charger_données()
        selected_row = df.iloc[index]
        entry_nom.delete(0, tk.END)
        entry_nom.insert(0, selected_row['Nom'])
        entry_age.delete(0, tk.END)
        entry_age.insert(0, selected_row['Âge'])
        entry_ville.delete(0, tk.END)
        entry_ville.insert(0, selected_row['Ville'])
    except IndexError:
        pass
# Fonction pour modifier les données du tableau
def modification():
    try:
        index = listbox.curselection()[0]
    except IndexError:
        messagebox.showwarning("Erreur", "Veuillez sélectionner une ligne.")
        return

    nom = entry_nom.get().strip()
    age = entry_age.get().strip()
    ville = entry_ville.get().strip()
    if not nom or not age or not ville:
        messagebox.showwarning("Erreur", "Tous les champs sont obligatoires.")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showwarning("Erreur", "L'âge doit être un nombre.")
        return

    df = charger_données()
    df.loc[index] = [nom, age, ville]
    enregistrer_données(df)
    mettreAJour_liste()
    vider_champs()
    messagebox.showinfo("Succès", "Modification effectuée avec succès.")
# Fonction pour supprimer les données dans la base de données
def supprimer_données():
    reponse = messagebox.askyesno('Confirmation','Voulez-vous supprimer cet enregistrement????')
    if reponse:
        try:
            index = listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("Erreur", "Sélectionnez une ligne à supprimer.")
            return

        df = charger_données()
        df.drop(index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        enregistrer_données(df)
        mettreAJour_liste()
        vider_champs()
        messagebox.showinfo("Succès", "Donnée supprimée avec succès.")
    else:
        messagebox.showinfo("Succès", "Suppression annulée")
# Fonction pour vider les champs après le chargement
def vider_champs():
    entry_nom.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_ville.delete(0, tk.END)
# Fonction pou permettre de faire la recherche
def rechercher():
    query = entry_recherche.get().strip().lower()
    listbox.delete(0, tk.END)
    df = charger_données()
    filtered_df = df[df.apply(lambda row: query in str(row['Nom']).lower() or query in str(row['Ville']).lower(), axis=1)]
    for i, row in filtered_df.iterrows():
        listbox.insert(tk.END, f"{i+1}. {row['Nom']} - {row['Âge']} - {row['Ville']}")
# Fonction pour exporter les données sous forme pdf
def exporter_données():
    df = charger_données()
    pdf_path = "C:/TPPYTHON/Listes_des_eleves.pdf"
    logo_path = "D:/ABOU FATIMA/Projets/Photoshop/image/logoIst.jpg"  # Remplace par le bon chemin si besoin

    # Données tableau
    data = [list(df.columns)] + df.values.tolist()
    styles = getSampleStyleSheet()
    current_time = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")

    elements = []
    title = Paragraph("REPUBLIQUE DE GUINEE", styles['Title'])
    elements.extend([title, Spacer(1, 12)])
    title = Paragraph("MINISTERE DE L'ENSEIGNEMENT SUPERIEUR DE LA RECHERCHE SCIENTIFIQUE ET DE L'INOVATION", styles['Title'])
    elements.extend([title, Spacer(1, 12)])
    
    if os.path.exists(logo_path):
        try:
            # Ouvrir l'image avec PIL pour récupérer sa taille
            pil_img = PILImage.open(logo_path)
            original_width, original_height = pil_img.size
            target_width = 60 * mm
            aspect_ratio = original_height / original_width
            target_height = target_width * aspect_ratio
    
            logo = Image(logo_path, width=target_width, height=target_height)
            logo.hAlign = 'CENTER'
            elements.append(logo)
            elements.append(Spacer(1, 12))
        except:
         pass  # en cas d'erreur, ignorer le logo
    # === TITRE ET DATE ===
    title = Paragraph("Liste des Enregistrements", styles['Title'])
    elements.extend([title, Spacer(1, 12)])

    # === TABLEAU ===
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # === FONCTION POUR LE PIED DE PAGE ===
    def ajouter_pied_de_page(canvas, doc):
        footer_time = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
        canvas.setFont("Helvetica", 9)
        canvas.drawString(15 * mm, 15 * mm, f"Page {canvas.getPageNumber()}")
        canvas.setFont("Helvetica-Bold", 9)
        canvas.drawCentredString(105 * mm, 15 * mm, "Pofesseur: Dr. Paul Python")
        canvas.drawRightString(200 * mm, 15 * mm, f"Date : {footer_time}")

    # === GÉNÉRATION DU PDF ===
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    doc.build(elements, onFirstPage=ajouter_pied_de_page, onLaterPages=ajouter_pied_de_page)

    messagebox.showinfo("Export PDF", f"PDF généré avec succès :\n{pdf_path}")


# === Interface graphique pour construire la fenêtre ===
fenetre = tk.Tk()
fenetre['background']='yellow'
centrer_fenetre(fenetre, 500, 500)
fenetre.resizable(False, False)

fenetre.title("GESTION D'INSCRIPTION EN PYTHON VERS EXCEL")

# Les champs de saisie
tk.Label(fenetre, text="Nom", width=15).place(x=10, y=5)

entry_nom = tk.Entry(fenetre)
entry_nom.place(x=150, y=5)

tk.Label(fenetre, text="Matricule", width=15).place(x=10, y=30)

entry_age = tk.Entry(fenetre)
entry_age.place(x=150, y=30)

tk.Label(fenetre, text="Ville", width=15).place(x=10, y=55)
entry_ville = tk.Entry(fenetre)
entry_ville.place(x=150, y=55)

# Boutons CRUD
tk.Button(fenetre, text="Insérer", width=10, command=inserer_données).place(x=10, y=100)
tk.Button(fenetre, text="Modifier", width=10, command=modification).place(x=190, y=100)
tk.Button(fenetre, text="Supprimer", width=10, command=supprimer_données).place(x=100, y=100)
tk.Button(fenetre, text="Vider", width=10, command=vider_champs).place(x=290, y=100)
#tk.Button(fenetre, text="Lire", width=25, command=mettreAJour_liste).grid(row=5, column=0, columnspan=2, pady=5)

# Les buttons Recherche et champ de saisi
tk.Label(fenetre, text="Recherche", width=9 ).place(x=290, y=30)
entry_recherche = tk.Entry(fenetre)
entry_recherche.place(x=370, y=30)
tk.Button(fenetre, text="Rechercher", width=16, command=rechercher).place(x=370, y=55)

# Liste des données
listbox = tk.Listbox(fenetre, width=50)
listbox.place(x=10, y=150)
listbox.bind('<<ListboxSelect>>', selectionner_liste)

# Boutton pour Exporter en PDF
tk.Button(fenetre, text="Exporter en PDF", width=16, command=exporter_données).place(x=10, y=330)

# Démarrer et lancer la fenêtre
mettreAJour_liste()
fenetre.mainloop()
