# -*- coding: utf-8 -*-
"""
Created on Thu May 22 00:42:36 2025

@author: abouf
"""

import mysql.connector

def connecter_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password="", 
        database="scolarite" 
    )

def creer_tables():
    conn = connecter_bd()
    curseur = conn.cursor()

    # Table eleves
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS eleves (
        id INT AUTO_INCREMENT PRIMARY KEY,
        matricule VARCHAR(20) UNIQUE,
        nom VARCHAR(50),
        prenom VARCHAR(50),
        age INT,
        ville VARCHAR(100),
        date_naissance DATE
    )
    """)

    # Table classes
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom_classe VARCHAR(50),
        annee_scolaire VARCHAR(20)
    )
    """)
    
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) UNIQUE NOT NULL,
            mot_de_passe VARCHAR(255) NOT NULL
            )
               """ )

    # Table inscription
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS inscription (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_eleve INT,
        id_classe INT,
        date_inscription DATE,
        FOREIGN KEY (id_eleve) REFERENCES eleves(id),
        FOREIGN KEY (id_classe) REFERENCES classes(id)
    )
    """)

    conn.commit()
    conn.close()
