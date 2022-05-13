import math

a, b, c = map(int, input().split())
g1 = math.gcd(a, b)
g2 = math.gcd(b, c)
g = math.gcd(g1, g2)
print(a//g + b//g + c//g - 3)
