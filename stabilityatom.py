A = int(input('A:'))
P = int(input('P:'))

a = 15.75
b = 17.8
y = 0.71
e = 23.7
x = 34

if (A-P)% 2 == 0 and P % 2 == 0:
    onlyo = +34
else:
    if A% 2 != 0:
        onlyo = 0
    else:
        onlyo = -34

Ec = a*A-b*(A**(2/3)) - y*((P**2)/(A**(1/3))) - e*(((A-2*P)**2)/A) + onlyo*A**(-3/4)
R = 1.3*A**(1/3)

print("Z: ",A/(1.98+0.015*A**(2/3)))
print(Ec,Ec/A)
print(str(R)+"* 10**-13")
print("Probability of Spontaneous Fission: ",P**2/A ,",45 ≈ 100%")
