X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
rx = 0
ry = 0
for i in range(3):
    if X.count(X[i]) < 2:
        rx = X[i]
    if Y.count(Y[i]) < 2:
        ry = Y[i]
print(rx, ry)