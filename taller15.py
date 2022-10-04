import numpy as np
A = np.array([[3,2,2],
              [3,1,-3],
              [1,0,-2]], dtype=float)
casicero = 1e-15
tamano = np.shape(A)
n = tamano[0]
identidad = np.identity(n)
AB = np.concatenate((A,identidad),axis=1)
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
    adelante = i+1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB[i,:] = AB[i,:]/AB[i,i]
inversa = np.copy(AB[:,n:])
print('Inversa de A: ')
print(inversa)
B = np.array([[1,2,0,4],
              [2,0,-1,-2],
              [1,2,-1,0],
              [0,4,1,0]], dtype=float)
casicero = 1e-15
tamano = np.shape(B)
n = tamano[0]
identidad = np.identity(n)
BB = np.concatenate((B,identidad),axis=1)
BB0 = np.copy(BB)
tamano = np.shape(BB)
n = tamano[0]
m = tamano[1]
for i in range(0,n-1,1):
    columna = abs(BB[i:,i])
    dondemax = np.argmax(columna)
    if (dondemax !=0):
        temporal = np.copy(BB[i,:])
        BB[i,:] = BB[dondemax+i,:]
        BB[dondemax+i,:] = temporal
BB1 = np.copy(BB)
for i in range(0,n-1,1):
    pivote = BB[i,i]
    adelante = i+1
    for k in range(adelante,n,1):
        factor = BB[k,i]/pivote
        BB[k,:] = BB[k,:] - BB[i,:]*factor
BB2 = np.copy(BB)
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = BB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = BB[k,i]/pivote
        BB[k,:] = BB[k,:] - BB[i,:]*factor
    BB[i,:] = BB[i,:]/BB[i,i]
inversa = np.copy(BB[:,n:])
print('Inversa de B: ')
print(inversa)