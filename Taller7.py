from ast import Num
import math 
import os
c=2
x=0
num=[]
print("VALOR APROXIMADO")

a=float(input("Ingrese un angulo en radianes: "))
i=math.cos(a)*(10**-8) * 100 #9.210609940028851e-07
y=100000
cosI=1
num.append(cosI)

while y>=i:
    t= ((a**c)/math.factorial(c))
    if x%2==0:
        t=t*-1
    cosA=num[x]+t
    x+=1
    c+=2
    num.append(cosA)
    y=abs((num[x]-num[x-1])/num[x])*100
print(F"Valor : {num[x]}\n %De Error: {y}")