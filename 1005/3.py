# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:41:45 2018

@author: ESFOT
"""



def leertxt():
    numeros =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    letras =["T","R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    mensaje =[numeros , letras]
    archi = open('3.txt','r+')
    cadena = archi.readline()
    print(numeros)
    #print (numeros[15] , numeros[8] , numeros[6] , numeros[9] , numeros[22] , numeros[1])
    archi.write(" 15 8 6 9 22 1")
    
    archi.close()
   
leertxt()