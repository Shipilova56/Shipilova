pr=1
for n in range(1,21):
    verh=(2*n-1)**(n/3)
    niz=(2**(n+1))*(2*n+1)
    pr=pr*(verh/niz)
print(pr)