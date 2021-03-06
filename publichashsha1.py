# -*- coding: utf-8 -*-
"""PublicHashSHA1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ocRuLEiMXZ6lr9aRNzAZzvf8qEayy3Mr

<table>
<thead>
  <tr>
    <th><img alt="UdeA" height="150px" src="https://upload.wikimedia.org/wikipedia/commons/archive/f/fb/20161010213812%21Escudo-UdeA.svg" align="left" hspace="10px" vspace="0px"></th>
    <th><h1> <b> Implementación del algoritmo SHA-1 "HASH Function" </b> </h1></th>
    <th><img alt="CC" height="150px" src="https://www.udea.edu.co/wps/wcm/connect/udea/b867d329-d2de-4a2f-b85f-81b3ea92e8a8/1.JPG?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_L8L8H8C0LODDC0A6SSS2AD2GO4-b867d329-d2de-4a2f-b85f-81b3ea92e8a8-mWZpYpQ" align="right" hspace="0px" vspace="0px"></th>
  </tr>
</thead>
<hr size=10 noshade color="green">
</table>
<hr size=10 noshade color="green">

<p>
<img alt="CC" height="70px" src="https://creativecommons.org/images/deed/cc_blue_x2.png" align="left" hspace="0px" vspace="0px">
<img alt="Attribution" height="70px" src="https://creativecommons.org/images/deed/attribution_icon_blue_x2.png" align="left" hspace="0px" vspace="0px">
<img alt="NC" height="70px" src="https://creativecommons.org/images/deed/nc_blue_x2.png" align="left" hspace="0px" vspace="0px">
<img alt="SA" height="70px" src="https://creativecommons.org/images/deed/sa_blue_x2.png" align="left" hspace="0px" vspace="0px">
</p>

<div align="right">
<h2> <b> Por: Julián Andrés Castillo G. </b> </h2>
<a href="mailto:jandres.castillo@udea.edu.co"> ✉ Julian Andres Castillo Grisales </a> 
</div><br><br>

<br>

**El presente documento hace parte del grupo de Investigación Ingeniería & Sociedad - Jornada de Conferencias.**
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 9 14:45:58 2021

@author: Julian Castillo
@script: Implementar SHA-1
"""

import hashlib

texto = "Ingeniería y Sociedad" #@param {type:"string"}

# Pasamos a Unicode el texto
# Luego se pasa a la funcion SHA1() de la libreria hashlib 
resultado = hashlib.sha1(texto.encode())
# Imprimir resultado solo me retorna la posición de memoria
print("Posición en Memoria -> ", resultado)
resultado = resultado.hexdigest()
# printing the equivalent hexadecimal value.
print("El valor hexadecimal de SHA1 es ->", resultado )
print("El largo de la cadena Hash es de", len(resultado), "caracteres")

"""Cadena de entrada: “Ingenieria y Sociedad”

Hash Salida: 8588b58bd1c2b1eaf09a7b3ff654da34f91d5830

Una Tilde de diferencia

Cadena de entrada: “Ingeniería y Sociedad”

Hash Salida: 862603d2331383690354d232f16fc073ab1d17e7
"""

cadena1 = '8588b58bd1c2b1eaf09a7b3ff654da34f91d5830' # --> “Ingenieria y Sociedad”
cadena2 = '862603d2331383690354d232f16fc073ab1d17e7' # --> “Ingeniería y Sociedad”
#Comparemos las cadenas una a una luego de ver su tipo de datos
print(type(cadena1))
print(type(cadena2))
igualdadposicional = 0
for i in range(len(cadena1)):
    if cadena1[i] == cadena2[i]:
        igualdadposicional +=1
print('Total de posiciones iguales: {} de un total de 40'.format(igualdadposicional))
print('\tEsto equivale a un {:,.2f}%'.format(igualdadposicional/len(cadena1)*100))