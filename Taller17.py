import os
import numpy as np
isActive=True
print("Elija su opcion")
print("1-MÍNIMOS CUADRADOS 2-MODELO EXPONENCIAL 3-SALIR")
while isActive:
    os.system('pause')
    os.system('cls')
    print("REGRESIONES")
    op=int(input(""))
    if op==1:
        xy=[]
        x2=[]
        x=[1,2,3,4,5,6,7,8]
        y=[7,5,6,3,4,2.6,2,0.6]
        sumx=sum(x)
        sumy=sum(y)
        promx=(sumx/len(x))
        promy=(sumy/len(y))
        for i in range(len(x)):
            xy.append(x[i]*y[i])
        sumxy=sum(xy)
        for i in range(len(x)):
            x2.append(x[i]*x[i])
        sumx2=sum(x2)
        m=((len(x)*(sumxy))-(sumx*sumy)/((len(x)*sumx2)-(sumx*sumx)))
        b=float(promy-(m)*(promx))
        print(f"La ecuación de la recta es y = {m}x+({b})")
    elif op==2:
        x = np.array([1,2,3,4,5,6])
        y = np.array([4.5,6,9,12,17,24])
        logx = np.log(x)
        logy = np.log(y)
        coefficients = np.polyfit(x, logy, 1)
        print(f"La ecuación de la curva es y = {coefficients[0]}x+({coefficients[1]})")
    elif op==3:
        isActive=False