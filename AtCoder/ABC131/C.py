import math

a, b, c, d = map(int, input().split())
c_cnt = b // c - (a-1) // c
d_cnt = b // d - (a-1) // d
e = c*d // math.gcd(c, d)
e_cnt = b // e - (a-1) // e
print((b-a+1) - c_cnt - d_cnt + e_cnt)