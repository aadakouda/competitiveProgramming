n, k, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = k
for i in range(n):
    temp = a[i] // x
    if temp <= cnt:
        a[i] %= x
        cnt -= temp
    else:
        a[i] -= x*cnt
        cnt = 0
    if cnt == 0:
        break
a.sort(reverse=True)
if cnt == 0:
    print(sum(a))
else:
    if len(a) < cnt:
        print(0)
    else:
        print(sum(a[cnt:]))