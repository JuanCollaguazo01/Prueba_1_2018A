# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:24:12 2018

@author: ESFOT
"""

def creartxt(): 

    archi=open('1.txt','w') 

    archi.close() 
    
    archi2=open('1.1.txt','w') 

    archi2.close() 

def grabartxt(): 
     
    archi2=open('1.1.txt','a') 
    num='1'+'1'+'0'+'1'+'0'+'1'
    archi2.write(num) 
    
    archi2.close()
    
    archi=open('1.txt','a') 
    
    
        

     
    def leertxt (): 
        archi.write('Linea 15654654654')
        archi3=open('1.1.txt','r') 
        linea = archi3.readline
        
        if linea[0]==1:
            archi.write('Linea 1')
            r=linea[0]*(2*2*2*2*2)
        if linea[2]==1:
            archi.write('Linea 2')
            r2=linea[1]*(2*2*2*2)
        if linea[3]==0:
            archi.write('Linea 3')
            r3=linea[2]*(2*2*2)
        if linea[4]==1:
            archi.write('Linea 4')
            r4=linea[3]*(2*2)
        if linea[5]==0:
            archi.write('Linea 5')
            r5=linea[4]*(2)
        if linea[6]==1:
            archi.write('Linea 6')
            r6=linea[5]*(0)
            archi.write('la suma de binarios es: '+(r+r2+r3+r4+r5+r6))

        archi3.close()
    archi.close()
creartxt() 
grabartxt()
