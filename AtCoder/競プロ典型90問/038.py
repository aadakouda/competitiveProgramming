import math
a, b = map(int, input().split())
res = a*b//math.gcd(a, b)
print(res if res <= 10**18 else 'Large')