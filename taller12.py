import decimal
import math
from decimal import *
getcontext().prec = 50

h=0.005
xi=0.55
fx=math.e**-xi
vant=fx
c=0
for i in range(1,16):
    if i%2!=0:
        e=fx*-1
    else:
        e=fx
    c+=1
    vact=decimal.Decimal(vant) + decimal.Decimal((decimal.Decimal(e)*(decimal.Decimal((h)**c)))/math.factorial(c))
    ea=decimal.Decimal(abs((decimal.Decimal(vact)-decimal.Decimal(vant))/vact)*100)
    print(f"\nORDEN {i}:\n\nVALOR: {vact}\nERROR: {ea}%")
    vant=vact
