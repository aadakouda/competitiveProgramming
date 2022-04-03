a, b = map(int, input().split())
length = (a**2 + b**2) ** 0.5
rate = 1 / length
print(a*rate, b*rate)