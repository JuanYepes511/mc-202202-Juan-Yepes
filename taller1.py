A=set()
B=set()

continuar=0
cona=0
conb=0
while continuar==0:
    print("Indroduzca a continuacion el numero de elementos de cada conjunto")

    try:
        cona=int(input("Conjunto A :"))
        conb=int(input("Conjunto B :"))
    except ValueError:
        print("El valor dado no es valido")
        cona=0
        conb=0
    else:
        continuar = 1

print("Ingrese los elementos del conjunto A")
av=0
while av!=cona:
    xa=float(input(" "))
    A.add(xa)
    av=av+1
print("Ingrese los elementos del conjunto B")
bv=0
while bv!=conb:
    xb=float(input(" "))
    B.add(xb)
    bv=bv+1
o=0
while o==0:
    C=set()
    print("Seleccione que operacion desea realizar entre los conjuntos")
    print ("1. Union")
    print ("2. Interseccion")
    print("3.Diferencia")
    print("4.Diferencia simetrica")
    print("5.Cerrar programa")
    opcion=int(input("Elija su opcion: "))
    if opcion==1:
        C = (A|B)
        #C.add(r)
        print("El conjunto C esta formado por",C, "y su cardinalidad es", len(C))
        
    if opcion==2:
        C=(A&B)
        print("El conjunto C esta formado por",C, "y su cardinalidad es", len(C))
        
    if opcion==3:
        C=(A-B)
        print("El conjunto C esta formado por",C, "y su cardinalidad es", len(C))
        
    if opcion==4:
        C=(A^B)
        print("El conjunto C esta formado por",C, "y su cardinalidad es", len(C))
        
    if opcion==5:
        o=o+1



