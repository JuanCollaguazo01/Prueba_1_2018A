# -*- coding: utf-8 -*-
"""

"""
import math

def Volumen_Cubo(a): # arista al cubo
    return a * a * a
 
def Volumen_Piramide_Triangular(a, b): # (area de la base * altura)/3 
    return (a*b)/3
 
def Volumen_Esfera(a): # 4/3 * Pi * r^3
    return 4/3*math.pi*(a*a*a)
 
print("Opciones\n1.- Cubo\n2.- Piramide Base Triangular \n3.- Esfera")


operaciones = { '1': Volumen_Cubo, '2': Volumen_Piramide_Triangular, '3': Volumen_Esfera}
 
seleccion = input('Escoge una: ')

if seleccion=='1':
    print('Usted esta en el Cubo')
    num1 = input("Ingrese Arista: ")
    resultado = operaciones[seleccion](int(num1))
    print(resultado)

elif seleccion=='2':
    print('Usted esta en la Piramide Base Triangular')
    num1 = input("Ingrese Altura: ")
    num2 = input("Ingrese base: ")
    resultado = operaciones[seleccion](int(num1),int(num2))
    print(resultado)

elif seleccion=='3':
    print('Usted esta en la esfera')
    num1 = input("Ingrese el Radio: ")
    resultado = operaciones[seleccion](int(num1))
    print(resultado)

else:
    print("Esa no vale")

    
