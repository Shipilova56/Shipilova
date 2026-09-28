from math import sin,pi,factorial
s=0
for n in range(1,51):
    s+= sin(n*pi/2) / (2*n**n+factorial(n))
print(s)