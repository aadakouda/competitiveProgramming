n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    temp = list(map(int, input().split()))
    c.append(temp[0])
    a.append(temp[1:])
min_price = float('inf')
for i in range(2**n):
    u = [0] * m
    p = 0
    for j in range(n):
        if (i >> j) & 1:
            p += c[j]
            for k in range(m):
                u[k] += a[j][k]
    if all([u[j] >= x for j in range(m)]):
        min_price = min(min_price, p)

if min_price == float('inf'):
    print(-1)
else:
    print(min_price)