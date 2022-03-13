n = int(input())
X = []
Y = {}
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    if y in Y:
        Y[y].append(i)
    else:
        Y[y] = [i]
s = input()
flg = False
for key in Y.keys():
    if flg:
        break
    if len(Y[key]) >= 2:
        R = []
        L = []
        for v in Y[key]:
            if s[v] == 'R':
                R.append(X[v])
            else:
                L.append(X[v])
        if len(R) > 0 and len(L) > 0 and min(R) < max(L):
            flg = True
print('Yes' if flg else 'No')