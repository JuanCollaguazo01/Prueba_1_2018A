# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:24:12 2018

@author: ESFOT
"""

def reverse(list):
    if len(list)==1:
        return list
    else:
        return list[-1]+reverse(list[:-1])

def creartxt(): 

    archi=open('2.txt','w') 

    archi.close() 

def grabartxt(): 

    archi=open('2.txt','a') 
    
    archi.write("\nInviertir el contenido de una cadena de texto y guárdelo en un archivo de texto \n \n ") 
    
    n = input("Ingrese la cadena de texto: ")

    archi.write("Tu cadena de texto es: \n "+n+"\n") 

    archi.write("Tu cadena de texto invertida es: \n "+reverse(n))

    archi.close() 
creartxt() 

grabartxt()