import math 
import os
repetir=True
while repetir:
    print("VALOR APROXIMADO")  
    print("Seleccione el punto que desea")
    print("1 - SERIE DE MACLAURIN #1")
    print("2 - SERIE DE MACLAURIN #2")
    print("3 - Salir")
    op=int(input(""))
    if op==1:
        mc=2
        a=0
        x=0.85
        eulers=[]
        Es=0.5*(10**-8) * 100
        pe=100000
        eu=1-x
        eulers.append(eu)
        while pe>=Es:
            fracc=(x**mc)/math.factorial(mc)
            if a%2!=0:
                fracc=fracc*-1
            e=eulers[a]+fracc
            a+=1
            mc+=1
            eulers.append(e)
            pe=abs((eulers[a]-eulers[a-1])/eulers[a])*100
        print(f"VALOR: {eulers[a]}  ERROR: {pe}  ITERACIONES: {a}  ÚLTIMO ERROR APROX: {pe}")
    elif op==2:
        mc=2
        a=0
        euler=[]
        x=0.85
        print("CALCULADORA DE VALOR APROXIMADO")
        Es=0.5*(10**-8) * 100 
        pe=100000
        eu=1+x
        euler.append(eu)
        while pe>=Es:
            fracc=(x**mc)/math.factorial(mc)
            e=euler[a]+fracc
            a+=1
            mc+=1
            euler.append(e)
            pe=abs((euler[a]-euler[a-1])/euler[a])*100
        r=1/euler[a]
        print(f"VALOR: {r}  ERROR: {pe}  ITERACIONES: {a}  ÚLTIMO ERROR APROX: {pe}")
    elif op==3:
        print("Muchas gracias por preferirnos")
        repetir=False