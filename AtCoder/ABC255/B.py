n, k = map(int, input().split())
a = list(map(int, input().split()))
a = set([i-1 for i in a])
z = []
for i in range(n):
    x, y = map(int, input().split())
    z.append((x, y))
ma = -1
for i in range(n):
    if i in a:
        continue
    x, y = z[i]
    ma = max(ma, min([abs((x-z[j][0])**2 + (y-z[j][1])**2) for j in a]))
print(ma**0.5)