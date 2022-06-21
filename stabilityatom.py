import math
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import time


A=int(input('A:'))
P=int(input('P:'))

a=15.75
b=17.8
y=0.71
e=23.7
x=34

if (A-P)% 2 == 0 and P % 2 == 0:
    onlyo=+34
else:
    if A% 2 != 0:
        onlyo=0
    else:
        onlyo=-34


Ec=a*A-b*(A**(2/3)) - y*((P**2)/(A**(1/3))) - e*(((A-2*P)**2)/A) + onlyo*A**(-3/4)
summaelect=0
summaelect2=0
g=(8.9875517873681764*10**9)*((-1.602176634*10**-19)**2)
R=1.3*A**(1/3)

V=50
ab=0.5
xarray=[]
yarray=[]
yarray2=[]
for r in range(1,1000):
    r=r/100
    summaelect=-V/(1+math.e**((r-R)/ab))
    y=0.7*r
    summaelect2= -10.463 *(math.e**y)/y -1650.6 *(math.e**y)/y +6484.2 *(math.e**y)/y
    yarray2.append(summaelect2*0.0001)
    xarray.append(r)
    yarray.append(summaelect)



print("Z: ",A/(1.98+0.015*A**(2/3)))


r=0.001
print("Force",-V/(1+math.e**((r-R)/ab)))
print("Force",-(V/ab) *math.e**(-r/ab)/(1-math.e**(-r/ab)))

print(Ec,Ec/A)
print(str(R)+"* 10**-13")
print("Probability of Spontaneous Fission: ",P**2/A ,",45 ≈ 100%")

plt.plot(xarray, yarray,label='x' )
plt.plot(xarray, yarray2,label='x2' )
plt.axis([-100, 100, -100, 100])
plt.show()
