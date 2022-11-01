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
x=[1,1,2,3,1,2,3,3]
y=[-1,0,0,1,1,2,2,0]
z=[1.6,3,1.1,1.2,3.2,3.3,1.7,0.1]
Sr=0
sumz=0
sumxz=0
sumyz=0
sumx=0
sumx2=0
sumxy=0
sumy2=0
sumy=0 
n=len(x)
for i in range(len(x)):
    sumz+= z[i]
    sumxz+=z[i]*x[i]
    sumyz+=z[i]*y[i]
    sumx+= x[i]
    sumx2+=x[i]**2
    sumxy+=x[i]*y[i]
    sumy2+=y[i]**2
    sumy+= y[i]
A = np.array([[n,sumx,sumy],
             [sumx,sumx2,sumxy],
             [sumy,sumxy,sumy2]])
B = np.array([[sumy],
             [sumxz],
             [sumyz]])
print(GAUSS(A,B))
a0=GAUSS(A,B)[0]
a1=GAUSS(A,B)[1]
a2=GAUSS(A,B)[2]
Sr=0
for i in range(len(x)):
    Sr+=(z[i]-a0-a1*x[i]-a2*y[i])**2
print(f"La función resultante es y = {a0} + {a1}x1 + {a2}x2 + e")
print(f"El coeficiente de correlación es {Sr}")