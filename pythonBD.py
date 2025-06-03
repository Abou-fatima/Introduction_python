# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 10:34:29 2025

@author: abouf 
"""
# 1 enquetes et formulaire en passant par les questionnaires
# 2 Collecte des données
# 3 Traitement des données
#      données manquantes
#      données adherantes
#  Exercices gestionnaire des données manquantes

import pandas as pd
data = pd.read_excel('C:/TPPYTHON/Donnees.xlsx') # Le chemin du fichier excel
print(data)

# affichage des 5 premieres lignes 
print(data.head())


try:
    dataNom = data['Nom']# Extraire la liste des noms dans le tableau
    print(dataNom)
except KeyError:
    print("###########################")
    print("Cette colonne n'existe pas dans la table")



dataAgeNom = data[['Nom','Age']]# Extraction de Nom et Age
print(dataAgeNom)


data1 = data[['Poids','Taille','Age']]# Extraire des calcules des statistiques descriptives
print(data1)
print(data1.describe())

# Un autre exemple
data2 = data[['Poids','Taille','Age','laffidi']]
print(data2)
print()
print(data2.describe())


data_filtration1 = data[data['Age']>23]# extraire les etudiants qui ont un age supeieur à 23 ans
print("Les etudiants qui ont un age > 23 ans sont :")
print(data_filtration1)


data_filtration2 = data_filtration1[['Age','Nom']] # compter le nombre d'etudiants qui ont un âge > 23 ans
print(data_filtration2.count())




#
data_filter4 = data[(data['Age']>23) & (data['laffidi']>=2)]
print(data_filter4)
print(data_filter4.count())


data_filter5 = data_filter4[['Nom','Age','laffidi']]
print(data_filter5)
print(data_filter5.count())



data_filter5.to_excel('C:/TPPYTHON/data_filtrage.xlsx',index=False, sheet_name='feuille1')
print(data_filter5)

data_filter4.to_excel('C:/TPPYTHON/data_filtrage.xlsx',index=False, sheet_name='feuille2')




#  Utilisation des matrices on utilise les mots clées (loc) et (iloc)
datanom = data.iloc[:,[1,4]]
print(datanom)


datanoms = data.iloc[6:11,4:6]#exercices afficher les etudiants comprises entre la 6 et 10 lignes et les colonnes comprises entre l'age et laffidi
print(datanoms)


datacolonne = data.iloc[:,-1]# afficher la derniere colonnes
print(datacolonne)


daata = data.iloc[:,:-1]# afficher toutes les colonnes sauf la derniere colonnes
print(daata)



daata = data.iloc[:-1,:]# Afficher les deux derniers lignes
print(daata)

# Extraire l'age et construire le diagramme en bas de l'age
import matplotlib.pyplot as plt

age = data[(data['Age']>13)]
print(age)


x = ['Guinée','Senegal','Mali','Liberia','Côte d\'ivoire','Togo','Nigeria']
y = [12,15,46,72,4,44,2]

plt.bar(x,y)
plt.title('Distribution des pays par PIB')
plt.xlabel('Les pays')
plt.ylabel('les PIB')
plt.show()



########################################################

import matplotlib.pyplot as plt
from collections import Counter
age = data['Age']

age_count = Counter(age)

x = list(age_count.keys())
y = list(age_count.values())
plt.hist(age,bins=range(min(age), max(age) + 2), edgecolor="black")
#plt.bar(x, y, color='red')

plt.xlabel('Ages')
plt.ylabel('Effectifs')
plt.title('Diagrammes d\'ages')
plt.show()



############################################


import matplotlib.pyplot as plt
from collections import Counter
 
T =[-2,-2,2,3,4,2,2,5,5,6,6,6,6]
frequence = Counter(T)
print("Frequence: ",frequence)
valeur = list(frequence.keys())

print("Valeur : ", valeur)
effectifs = list(frequence.values())
print("effectifs : ",effectifs)
plt.bar(valeur, effectifs)
plt.title("DIAGRAMME DE BARRE")
plt.xlabel("Valeur")
plt.ylabel("Effectifs")
plt.show()


##########♠   Analyse des correlation lineaire ##########

# correlation  entre le poids et la taille

import numpy as np 
x = data['Taille']
y = data['IMC']
covxy = np.cov(x,y) # covariance
print(covxy)

"""
[[ 4.65928571e-02 -1.42121646e+00]
 [-1.42121646e+00  6.48938309e+01]]

"""

##########   coefficient des correlation lineaire ##########

corData = data[['Age','IMC']]
corrxy = corData.corr()
print(corrxy)

"""
          Age       IMC
Age  1.000000  0.153882
IMC  0.153882  1.000000

"""

corData1 = data[['Poids','IMC']]
corrxy1 = corData1.corr()
print(corrxy1)


"""
          Poids       IMC
Poids  1.000000  0.281267
IMC    0.281267  1.000000

"""


corData2 = data[['Taille','IMC']]
corrxy2 = corData2.corr()
print(corrxy2)


"""
          Taille       IMC
Taille  1.000000 -0.817333
IMC    -0.817333  1.000000

"""


corData3 = data[['Taille','Poids']]
corrxy3 = corData3.corr()
print(corrxy3)


"""
          Taille     Poids
Taille  1.000000  0.287182
Poids   0.287182  1.000000

"""



x1 = data['Poids']
y1 = data['Taille']
covx1y1 = np.cov(x1,y1)
print(covx1y1)


"""
[[1.09057143e+02 6.47357143e-01]
 [6.47357143e-01 4.65928571e-02]]
"""


covx2y2 = corrxy3.iloc[0, 1]
print(covx2y2)



varx1 = x1.var()
print(varx1)




print('calcul de la droite ')
a = covx1y1/varx1
print(a)

moyx1 = x1.mean()
moyY1 = y1.mean()

print(moyx1, moyY1)

b = moyY1-(a*moyx1)
print(b)





"""

y = ax+b
a = cov(x,y)/var(x)

b = moyenne(y) - a*moyenne(x)

"""

# tracer les points

import matplotlib.pyplot as plt
import numpy as np
plt.scatter(x1, y1,)
x2 = np.linspace(40,100,10)
y2 = (0.0059*x2)+1.2127
plt.plot(x2, y2)
plt.title("Nuage des points entre poids et IMC")
plt.xlabel('Pour le poids')
plt.ylabel('pour le IMC')
plt.show()



###############################
import matplotlib.pyplot as plt
import pandas as pd
try: 
    GestionArrivee = pd.DataFrame({
        "Heure" : [8,9,10,11,12,13,14,15],
        "NbreArrivee" : [12,10,5,2,10,20,15,19]
        })
    print(GestionArrivee)
    GestionArrivee.to_excel('C:/TPPYTHON/fichier.xlsx', index=False)

    dataArrivee = pd.read_excel('C:/TPPYTHON/fichier.xlsx')
    print(dataArrivee)
    # Extraction des heures et du nombres d'arrivee
    X = dataArrivee['Heure']
    Y = dataArrivee['NbreArrivee']

    #plt.plot(X, Y) 
    plt.bar(X,Y)
    plt.xlabel('Heure d\'arrivée')
    plt.ylabel('Nombre d\'arrivée')
    plt.show()  
except FileNotFoundError:
    print("Le chemin du fichier n'existe pas")

#####################################
"""
def equation():
    
    a = float(input("Valeur de a : "))
    b = float(input("Valeur de b : "))

    if(a==0):
        if(b==0):
            print('infiité de solution')
        else:
            print('Pas de solution')
    else:
        x = -b/a
        print("la solution est ",x)
equation()
"""


import math 
def equation_premier_degre(a, b):
    """Résout une équation du premier degré ax + b = 0"""
    if a == 0:
        if b == 0:
            print("Infinité de solutions")
        else:
            print("Pas de solution")
    else:
        x = -b / a
        print(f"La solution est : {x:.2f}")

def equation_second_degre(a, b, c):
    """Résout une équation du second degré ax² + bx + c = 0"""
    if a == 0:
        # Si a = 0, c'est une équation du premier degré
        equation_premier_degre(b, c)
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Les solutions sont :",round(x1,2) , " et ",round(x2,2))
        elif delta == 0:
            x0 = -b / (2 * a)
            print("La solution unique est :", x0)
        else:
            print("Pas de solution dans R (solutions complexes)")

# Demander les coefficients
a = float(input("Valeur de a : "))
b = float(input("Valeur de b : "))
c = float(input("Valeur de c : "))

# Résolution de l'équation
equation_second_degre(a, b, c)






















