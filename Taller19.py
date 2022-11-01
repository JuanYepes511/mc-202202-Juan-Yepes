def REGRESION(x=list,y=list):
        xy=[]
        x2=[]
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
        b=promy-m*promx
        print(f"La ecuación de la recta de la regresión lineal es y = {m}x+({b})")
        return [m,b]
from math import sqrt
import os
import numpy as np
isActive=True
print("Elija su opcion")
print("1-MÍNIMOS CUADRADOS 2-MODELO EXPONENCIAL 3-ECUACIONES DE POTENCIA O RAZONES DE CRECIMIENTO 4- DESVIACION,ERROR Y COEFICIENTE 5-SALIR")
while isActive:
    os.system('pause')
    print("REGRESIONES")
    op=int(input(""))
    if op==1:
        x=[1,2,3,4,5,6,7,8]
        y=[7,5,6,3,4,2.6,2,0.6]
        REGRESION(x,y)
    elif op==2:
        x = np.array([1,2,3,4,5,6])
        y = np.array([4.5,6,9,12,17,24])
        logx = np.log(x)
        logy = np.log(y)
        coefficients = np.polyfit(x, logy, 1)
        print(f"La ecuación de la curva de la regresión por modelo exponencial es y = {coefficients[0]}x+({coefficients[1]})")
    elif op==3:
        pass
    elif op==4:
        x=[1,2,3,4,5,6,7]
        y=[0.2,0.6,1.6,3.5,5.5,9.1,13]
        sumxy=0
        sumx2=0
        Sr=0
        St=0
        sumx=sum(x)
        sumy=sum(y)
        promx=(sumx/len(x))
        promy=(sumy/len(y))
        for i in range(len(x)):
            sumxy+=x[i]*y[i]
        for i in range(len(x)):
            sumx2+=x[i]*x[i]
        m=((len(x)*(sumxy))-(sumx*sumy)/((len(x)*sumx2)-(sumx*sumx)))
        b=promy-m*promx
        for i in range(len(y)):
            St+=(y[i]-promy)**2
        Sy=sqrt((St)/(len(x)-1))
        for i in range(len(x)):
            Sr+=(y[i]-b-m*x[i])**2
            print(i)
        sy_x=sqrt((Sr)/(len(x)-2))
        print(Sr)
        print(b, m)
        r=sqrt(abs((St-Sr))/(St))*100
        print(f"La ecuación de la recta en la regresión lineal es y = {m}x+({b})")
        print(f"La desviación estándar es {Sy}, el error estándar es {sy_x}, y el coeficiente de correlación es {r}")
    elif op==5:
        isActive=False