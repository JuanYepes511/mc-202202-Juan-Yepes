import os
def PRODUCTO_MATRICES(a,b):
    filas_a = len(a)
    filas_b = len(b) 
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto
def CONSTRUCTOR_VECTORES(n):
    Vector=[]
    for i in range(0,n):
        valor = int(input(f"\nIngrese el valor de la posición n. {i+1}: "))
        Vector.append(valor)
    return Vector
def PRODUCTO_VECTORES(a:list,b:list,n):
    R=0
    for i in range(0,n):
        R+= a[i]*b[i]
    return R
def CONSTRUCTOR_MATRIZ(filas:int,columnas:int): 
    lista=[]
    matriz=[]
    for i in range(0,filas):
        for j in range(0,columnas):
            valor=int(input(f"\nIngrese el valor no. {j+1} de la fila {i+1}: "))
            lista.append(valor)
        matriz.append(lista)
        lista=[]
    return matriz
def MATRIZ3A(m):
    R=m
    for i in range(len(MatrizA)):
        for k in range(len(MatrizA[i])):
            R[i][k]=3*m[i][k]
    print(f"La respuesta es {R}")
def MATRIZ4B(m):
    R=m
    for i in range(len(MatrizA)):
        for k in range(len(MatrizA[i])):
            R[i][k]=4*m[i][k]
    print(f"La respuesta es {R}")
def MATRICES_SUMAR(a,b):
    R=a
    for i in range(len(a)):
        for k in range(len(a[i])):
            R[i][k]=a[i][k]+b[i][k]
isActive=True
menu2=["3A","4B","A+B","BxA"]
while isActive:
    os.system('cls')
    op=int(input("\nMENU\n\n1 - PRODUCTO VECTORES\n\n2 - MATRICES\n\n3 - SALIR\n\n\n\)_ "))
    if op==1:
        os.system('cls')
        print("VECTORES:\n\n")
        n=int(input("Ingrese la longitud de los dos vectores: "))
        print("\n\n1.\n\n")
        Vector1=CONSTRUCTOR_VECTORES(n)
        print("\n\n2.\n\n")
        Vector2=CONSTRUCTOR_VECTORES(n)
        print(f"El resultado del producto escalar entre ambos vectores es {PRODUCTO_VECTORES(Vector1,Vector2,n)}")
        os.sytem('pause')
    elif op==2:
        os.system('cls')
        print("MATRICES:")
        m1=int(input("Ingrese el numero de filas para la primera matriz: "))
        n1=int(input("Ingrese el numero de columnas para la primera matriz: "))
        m2=int(input("Ingrese el numero de filas para la segunda matriz: "))
        n2=int(input("Ingrese el numero de columnas para la segunda matriz: "))

        MatrizA=CONSTRUCTOR_MATRIZ(n1,m1)
        MatrizB=CONSTRUCTOR_MATRIZ(n1,m2)

        print(MatrizA)
        print(MatrizB)

        for i in range(len(menu2)):
            print(f"{i+1} - {menu2[i]}")
        op2=int(input("\)_"))
        if op2==1:
            MATRIZ3A(MatrizA)
        elif op2==2:
            MATRIZ4B(MatrizB)
        elif op2==3:
            if m1==m2 and n1==n2:
                print(f"La matriz resultado es {MATRICES_SUMAR(MatrizB,MatrizA)}")
            else:
                print("No se puede realizar la operación ya que las matrices no coinciden en tamaño")
        elif op2==4:
            if PRODUCTO_MATRICES(MatrizB,MatrizA)!=None:
                print(f"La matriz respuesta es {PRODUCTO_MATRICES(MatrizB,MatrizA)}")
            else: 
                print("La operación no se puede realizar")
        os.system('pause')
    elif op==3:
        print("Salir")
    isActive=False