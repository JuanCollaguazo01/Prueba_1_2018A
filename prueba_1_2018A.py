# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:22:13 2018

@author: Fernando Sanmartin
"""


def Volumen_Cubo(a):
    return a * a * a
 
def restar(a, b):
    return a - b
 
def multiplicar(a, b):
    return a * b;
 
num1 = input("Ingrese Arista: ")

 
print("Opciones\n1.- Volumen Cubo\n2.- Restar\n3.- Multiplicar")
 
operaciones = { '1': Volumen_Cubo, '2': restar, '3': multiplicar}
 
seleccion = input('Escoge una: ')
try:
    resultado = operaciones[seleccion](int(num1))
    print (resultado)
except:
    print("Esa no vale")