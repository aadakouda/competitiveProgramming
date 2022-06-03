import math

n, x, y = map(int, input().split())
x_cnt = n // x
y_cnt = n // y
z = x * y // math.gcd(x, y)
z_cnt = n // z
print(x_cnt + y_cnt - z_cnt)