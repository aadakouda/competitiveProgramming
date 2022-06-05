n = int(input())
s = []
t = []
d = {}
for i in range(n):
    S, T = map(str, input().split())
    s.append(S)
    t.append(T)
    if S in d:
        d[S].add(i)
    else:
        d[S] = {i}
    if T in d:
        d[T].add(i)
    else:
        d[T] = {i}

flg = True

for k, v in d.items():
    if len(v) > 1:
        for i in v:
            if len(d[s[i]]) > 1 and len(d[t[i]]) > 1:
                flg = False

print('Yes' if flg else 'No')