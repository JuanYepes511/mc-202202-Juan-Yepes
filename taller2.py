from abc import ABC
from re import A
def conjunto1():
    A=set()
    n=4
    while n<=19:
        n=n+1
        A.add(n)
    return A
def conjunto2():
    B=set()
    z= 0
    while z<23:
        z=z+2
        B.add(z)
    return B
def conjunto3():
    C=set()
    C.add(1)
    C.add(4)
    C.add(8)
    C.add(10)
    C.add(12)
    C.add(15)
    C.add(18)
    C.add(20)
    return C
def conjunto4():
    D=set()
    b= 0
    while b < 45:
        for i in range(2,46):
            x=2
            primo= True
            while primo and x < i:
                if i % x == 0:
                    primo = False
                else:
                    x = x+1
            if primo:
                D.add(i)
        b=b+1
    return D
A=conjunto1()
B=conjunto2()
C=conjunto3()
D=conjunto4()
o1= (B&(C^D))
o2= ((A&C)|B)
o3= ((B|D)-C)
o4= ((A-B)^(A&D))
print("Bienvenido al programa de operaciones entre conjuntos")
print("A continuacion se tienen los conjuntos A, B, C, D siendo: ")
print("A= ", A)
print("B= ", B)
print("C= ", C)
print("D= ", D)
print("A continuacion las operaciones")
print("Operacion 1 = B ∩ (C Δ D)")
print ("El resultado es: ", o1)
print("Operacion 2 = (A ∩ C) ∪ B)")
print ("El resultado es: ", o2)
print("Operacion 1 = (B ∪ D) - C")
print ("El resultado es: ", o3)
print("Operacion 1 = (A - B) Δ (A ∩ D)")
print ("El resultado es: ", o4)