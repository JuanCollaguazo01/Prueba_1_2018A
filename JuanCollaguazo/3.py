# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:24:23 2018

@author: ESFOT
"""
def cod(): 
    cad=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    return cad
    
def creartxt(): 

    archi=open('3.txt','w') 

    archi.close() 

def grabartxt(): 

    archi=open('3.txt','a') 
    n=input("Ingrese su mensaje para ser codifucado: \n")
    archi.write('Linea 1\n'+n) 
    
    archi.write('Su mensaje codificado es: \n'+cod(n))

    archi.close() 
creartxt() 
grabartxt()