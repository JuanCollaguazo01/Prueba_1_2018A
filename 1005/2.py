# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:24:54 2018

@author: ESFOT
"""
def leertxt():
   archi = open('2.txt','r+')
   cadena = archi.readline()
   archi.write("\n" + "estan" + " como" + " mundo" + " Hola")
   print(cadena)
   archi.close()
   
leertxt()