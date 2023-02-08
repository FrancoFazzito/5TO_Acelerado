# -*- coding: utf-8 -*-
"""Funcion de Shockley.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13WL8aSHO9rv9JbZvGkN4AIG3xhy2GtSD

Ecuacion de Shockley

![ecuacion shockley2.png](data:image/png;base64,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)
"""

import math
import matplotlib.pyplot as plt

#Constante
e=math.e #(Constante)
k=1.380649e-23 #Constante de Boltzmann (Constante)
q=1.6e-19 #Carga del electron (Constante)

#Variables
Is=1.00e-8 #Corriente de saturacion
n=1 #factor de idealidad de los materiales 2 silicio - 1 germanio
T=300 #temperatura en kelvin
resultados={}
precision=5 # Puntos tomados por Volt

def calcularEcuacionShockley(tension):
  #Realizamos los calculos
  qVd= (q*tension)
  NKT= (n*k*T)
  E= e**(qVd/NKT) # ** potencia
  I= Is*(E-1)*1000 #pasaje de Miliampere a ampere
  return I
  
for i in range(precision*8): # 1 es por un limite de 1V
  tension= i/(precision*10)
  resultado= calcularEcuacionShockley(tension)
  resultados[str(tension)]= resultado
print(resultados)

screen_size = [30,10]

fig, ax = plt.subplots(figsize=(screen_size[0], screen_size[1]))
ax.plot(list(resultados.keys()), list(resultados.values())) #key -> tension y la value -> resultado

plt.xlabel('X (Tensión/Volts)')
plt.ylabel('Y (Corriente/Ampere)')
plt.ylim(0,2.5)
plt.title('Función de Shockley')

plt.show()