# -*- coding: utf-8 -*-
"""
Created on Mon May 12 12:24:17 2025

@author: LENOVO T 470 S
"""

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS dbEtudiant")

conn.database = "dbEtudiant"

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Etudiant (
        matricule INT PRIMARY KEY,
        nom VARCHAR(100),
        age INT,
        ville VARCHAR(100)
    )
""")

etudiants = [
    (1001, "Alpha Ousmane Bah", 25, "Guinée"),
    (1002, "Oumar bah", 21, "Mamou"),
    (1003, "Abdoulaye Diallo", 23, "Kankan"),
    (1004, "Alseyni Sow", 20, "Labe"),
    (1005, "Sadio Diallo", 19, "Dalaba"),
]

sql = "INSERT INTO Etudiant (matricule, nom, age, ville) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, etudiants)
conn.commit()

print("Les données sont inserées avec succès")
print(f"{cursor.rowcount} enregistrements insérés dans la table Etudiant.")


cursor.close()
conn.close()