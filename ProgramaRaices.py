import os
isActive=True
def raices(n):
    x = n / 2
    for i in range(20):
        if x * x  == n:
            return x 
        else: 
            x = (x + (n/x)) / 2
    return x
while isActive:
    os.system('cls')
    print("CALCULADORA DE RAÍCES")
    print("1- Iniciar Calculadora")
    print("2- Salir")
    op1 = input("")
    if op1==1:
        base=int(input("Ingrese un número :"))
        if base <= 0:
            print("Este numero no tiene raiz")
        else:
            print(f"El resultado es {raices(base)}")

    if op1==2:
        isActive=False
