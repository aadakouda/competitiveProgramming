n, q = map(int, input().split())
a = list(map(int, input().split()))
idx = [i for i in range(n)]
t = [input() for _ in range(q)]
cnt = 0
for i in range(q):
    ti, x, y = map(int, t[i].split())
    x = (x-1 - cnt) % n
    y = (y-1 - cnt) % n
    if ti == 1:
        a[x], a[y] = a[y], a[x]
    elif ti == 2:
        cnt += 1
    elif ti == 3:
        print(a[x])