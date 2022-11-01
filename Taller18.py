from math import sqrt
import os
import numpy as np
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
        print(f"La ecuación de la recta es y = {m}x+({b})")
        return [m,b]
def MODELOEXP(x=list,y=list):
        logy = np.log(y)
        coefficients = np.polyfit(x, logy, 1)
        return coefficients
def ECUACIONES(x,y):
    logx = np.log(x,10)
    logy = np.log(y,10)
    coefficients = np.polyfit(logx,logy,1)
    return coefficients
def RAZONES(x,y):
    for i in range(len(x)):
         xinv=[]
         yinv=[]
         xinv.append(1/x[i])
         yinv.append(1/y[i])
         coefficients = np.polyfit(xinv,yinv,1)
         return coefficients
 
x=[1,3,5,7,9,11,13,15]
y=[2.1,3.2,3.8,4,4.2,4.4,4.5,4.7]
xnp=np.array(x)
ynp=np.array(x)
print("X-Y")
for i in range(len(x)):
    print(f"{x[i]}    -   {y[i]}")
print(f"Minimos Cuadrados: y = {REGRESION[0]}x+({REGRESION[1]})")
print(f"Modelo exponencial: y = {MODELOEXP(xnp,ynp)[0]}x+({MODELOEXP(xnp,ynp)[1]})")
print(f"Ecuanciones de potencia: y = {ECUACIONES(xnp,ynp)[0]}x+({ECUACIONES(xnp,ynp)[1]}")
print(f"Razon de cambio: y = {RAZONES(x,y)[0]}x+({RAZONES(x,y)[1]}")