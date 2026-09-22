import math
x=0.5
y=(math.acos(1-x**2)+math.asin(1-x**2))/math.sin(1-2*x**2)
print(y)