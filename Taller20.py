import numpy as np 
import os
casicero = 1e-15 
def GAUSS(A,B):
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]
    for i in range(0,n-1,1):
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        if (dondemax !=0):
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)
    ltfila = n-1
    ultcolumna = m-1
    for i in range(ltfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])
    return X
x=[0,1,2,3,4,5,6]
y=[-0.9,0,2,4.5,8.3,13,13,18]
Sr=0
sumy=0
sumx=0
sumx2=0
sumx3=0
sumx4=0
sumxy=0
sumx2y=0
n=len(x)
for i in range(len(x)):
    sumx+=x[i]
    sumx2+=x[i]*x[i]
    sumx3+=x[i]*x[i]*x[i]
    sumx4+=x[i]*x[i]*x[i]*x[i]
    sumy+=y[i]
    sumxy+=x[i]*y[i]
    sumx2y+=x[i]*x[i]*y[i]
A = np.array([[n,sumx,sumx2],
             [sumx,sumx2,sumx3],
             [sumx2,sumx3,sumx4]])
B = np.array([[sumy],
             [sumxy],
             [sumx2y]])
print(GAUSS(A,B))
a0=GAUSS(A,B)[0]
a1=GAUSS(A,B)[1]
a2=GAUSS(A,B)[2]
Sr=0
for i in range(len(x)):
    Sr+=(y[i]-a0-a1*x[i]-(a2*x[i]**2))**2
print(f"La función resultante es y = {a0} + {a1}x + {a2}x2 + e")
print(f"El coeficiente de correlación es {Sr}")

