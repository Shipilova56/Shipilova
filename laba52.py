n = int(input())
mx = -1000000
mn = 1000000
for i in range(1, n + 1):
    x = float(input())
    p = x * i
    s = x * i
    if p> mx:
        mx = p
    if s < mn:
        mn = s
print(mx)
print(mn)
