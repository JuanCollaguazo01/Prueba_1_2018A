# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:22:13 2018

@author: Fernando Sanmartin
"""


def Volumen_Cubo(a): # arista al cubo
    return a * a * a
 
def Volumen_Piramide_Triangular(a, b): # (area de la base * altura)/3 
    return a - b
 
def Volumen_Esfera(a, b): # 4/3 * Pi * r^3
    return a * b;
 
print("Opciones\n1.- Cubo\n2.- Piramide Base Triangular \n3.- Esfera")


operaciones = { '1': Volumen_Cubo, '2': Volumen_Piramide_Triangular, '3': Volumen_Esfera}
 
seleccion = input('Escoge una: ')

try:
    num1 = input("Ingrese Arista: ")
    resultado = operaciones[seleccion](int(num1))
    print (resultado)
except:
    print("Esa no vale")
    
    
