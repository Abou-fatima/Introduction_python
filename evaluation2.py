# -*- coding: utf-8 -*-
"""
Created on Mon May 19 21:55:08 2025

@author: abouf
"""
# Equation de la forme ax+b=0
a= int(input("Donnez la valeur de a: "))
b= int(input("Donnez la valeur de b: "))
if a==0:
    print("Pas de solution")
else:
    print("La solution est : ",-b/a)

# Equation de la forme ax²+bx+c=0
import math
a= int(input("Donnez la valeur de a: "))
b= int(input("Donnez la valeur de b: "))
c= int(input("Donnez la valeur de c: "))
delta = b*b-4*a*c
if(delta<0):
    print('Pas de solution dans R')
elif(delta==0):
    print("La solution double est :", -b/2*a)
else:
    x1 = -b-math.sqrt(delta)/2*a
    x2 = -b+math.sqrt(delta)/2*a
    print("Les solutions sont :x1= ",x1,"x2= ",x2)



#Somme des 30 premiers nombres entiers
somme = 0
for i in range(1, 31):
    somme +=i
print("La somme est ",somme)



# Construire une fonction f(x)=xsin(x), -3<=x<=3
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500)
fx = x*np.sin(x)
plt.plot(x, fx, label="f(x) =x*sin(x)",color='red')
plt.title("Courbe de f(x)=x*sin(x)")
plt.xlabel("X")
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.legend()
plt.show()



import numpy as np 
M= np.array((
    [2,5,6,5,5,5,],
    [78,68,3,5,55,5],
    [0,4,3,3,0,0],
    [1,0,0,1,1,4]
    ))
print(M[:,:-1])
print(M[:,-1])
print(M[:,0:2])
print(M[0:2,:])


T=[5,7,-6,9,4,3,0,8,9]
print(sum(T))
print(len(T))
print(T.remove(7))
print(T.append(10))
print(T)



import pandas as pd
import statistics as st
df = pd.read_excel("C:/TPPYTHON/evaluation2.xlsx")
q1 = df[['NombreAppel','DurreAppel']]
moy = st.mean(q1)
print(moy)
print(q1)
print(df)


q4 = df[(df['qualiteClient'])=='passable']
print(q4.count())



q3 = df[(df['TypeTel']=='samsung') & (df['NombreAppel']>=98)]
print(q3)



q2 = df[['NombreAppel','DurreAppel','TypeTel']]
print(q2)
