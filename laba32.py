import math
a=-0.7
b=0.7
step=0.05
for i in range(29):
    x=a+i*step
    y=(1+x)**((1+x)**2)/(1-x)**((1-x)**2)
    print(f"{x:2f}|{y:.5f}")