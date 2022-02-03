h, w = map(int, input().split())
S = [input() for _ in range(h)]
result = [['0'] * w for _ in range(h)]
dh = [-1, -1, -1, 0, 0, 1, 1, 1]
dw = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            for k in range(8):
                if -1 < i+dh[k] < h and -1 < j+dw[k] < w:
                    result[i+dh[k]][j+dw[k]] = str(int(result[i+dh[k]][j+dw[k]]) + 1)
for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            result[i][j] = '#'
for i in range(h):
    print(''.join(result[i]))