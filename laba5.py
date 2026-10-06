n = int(input("Введите количество чисел N:"))
total = 0
print("Введите числа:")
prev = float(input())
for i in range(n - 1):
    current = float(input())
    if prev > current:
        distance = prev - current
    else:
        distance = current - prev
        total =  total + distance
        prev = current
print("Сумма рассояний:", total)
