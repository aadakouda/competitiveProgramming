h, w = map(int, input().split())
s = [input() for _ in range(h)]
x = []
y = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            x.append(i)
            y.append(j)
print(abs(x[0]-x[1])+abs(y[0]-y[1]))