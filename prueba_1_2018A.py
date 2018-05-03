import os
import math


def Volumen_Cubo(a):  # arista al cubo
    print ('el volumen del cubo es: ')
    return a * a * a


def Volumen_Piramide_Triangular(a, b):  # (area de la base * altura)/3
    print('el volumen de la piramide triangular es: ')
    return (a * b) / 3


def Volumen_Esfera(a):  # 4/3 * Pi * r^3
    print('el volumen de la esfera es: ')
    return 4 / 3 * math.pi * (a * a * a)

operaciones = {'1': Volumen_Cubo, '2': Volumen_Piramide_Triangular, '3': Volumen_Esfera}




def menu():

    os.system('cls')  # Función que limpia la pantalla y muestra nuevamente el menu
    print(" ")
    print("Calculo de volumen de figuras geometricas")
    print("1 - Cubo")
    print("2 - Piramide Base Triangular")
    print("3 - Esfera")
    print("4 - salir")




while True:

    menu() # Mostramos el menu


    print("")
    opcionMenu = input("inserta un numero para elegir la opcion que desea: ") # solicitamos una opción al usuario
    seleccion = opcionMenu

    if opcionMenu == "1":
        print("")
        if seleccion == '1':
            print('Usted esta en el Cubo')
            num1 = input("Ingrese Arista: ")
            resultado = operaciones[seleccion](int(num1))
            print(resultado)

    elif opcionMenu == "2":
        print("")

        if seleccion == '2':
            print('Usted esta en la Piramide Base Triangular')
            num1 = input("Ingrese Altura: ")
            num2 = input("Ingrese base: ")
            resultado = operaciones[seleccion](int(num1), int(num2))
            print(resultado)

    elif opcionMenu == "3":
        print("")

        if seleccion == '3':
            print('Usted esta en la esfera')
            num1 = input("Ingrese el Radio: ")
            resultado = operaciones[seleccion](int(num1))
            print(resultado)

    elif opcionMenu == "4":
        break
    else:
        print("")
        input("seleccion incorrecta...\npulsa una tecla para continuar")