n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ad = {}
for i in range(n):
    if a[i] % 46 in ad:
        ad[a[i] % 46] += 1
    else:
        ad[a[i] % 46] = 1
bd = {}
for i in range(n):
    if b[i] % 46 in bd:
        bd[b[i] % 46] += 1
    else:
        bd[b[i] % 46] = 1
cd = {}
for i in range(n):
    if c[i] % 46 in cd:
        cd[c[i] % 46] += 1
    else:
        cd[c[i] % 46] = 1

cnt = 0
for ka, va in ad.items():
    for kb, vb in bd.items():
        for kc, vc in cd.items():
            if (ka+kb+kc) % 46 == 0:
                cnt += va*vb*vc
print(cnt)