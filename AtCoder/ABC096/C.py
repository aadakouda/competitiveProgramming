h, w = map(int, input().split())
S = [input() for _ in range(h)]
result = [[False] * w for _ in range(h)]
dh = [-1, 0, 0, 1]
dw = [0, -1, 1, 0]
for i in range(h):
    for j in range(w):
        if S[i][j] == '.':
            result[i][j] = True
        else:
            for k in range(4):
                ik = i+dh[k]
                jk = j+dw[k]
                if -1 < ik < h and -1 < jk < w and S[ik][jk] == '#':
                    result[i][j], result[ik][jk] = True, True
                    break
print('Yes' if all([all(r) for r in result]) else 'No')