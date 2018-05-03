# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:24:43 2018

@author: ESFOT
"""

def leertxt():
   archi = open('1.txt','r+')
   a=archi.readline()
   b=archi.readline()
   c=archi.readline()
   d=archi.readline()
   e=archi.readline()
   f=archi.readline()
   
   
   decimal = (1 * 32) + (1 * 16) + (0 * 8) + (1 * 4) + (0 * 2) + (1 * 1)
   print(decimal)
   archi.write('\nel desimal es =%s' % decimal)
   archi.close()

    
leertxt()
