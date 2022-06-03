n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
flg = False
for i in range(n):
    x1, y1 = p[i]
    for j in range(i+1, n):
        x2, y2 = p[j]
        for k in range(j+1, n):
            x3, y3 = p[k]
            if (y1-y2)*(x1-x3) == (y1-y3)*(x1-x2):
                flg = True
print('Yes' if flg else 'No')