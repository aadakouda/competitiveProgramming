h, w = map(int, input().split())
A = []
for i in range(h):
    a = list(map(int, input().split()))
    A.append(a)

col = [0]*w
for i in range(h):
    for j in range(w):
        col[j] += A[i][j]

result = [[sum(a)]*w for a in A]
for i in range(h):
    for j in range(w):
        result[i][j] += col[j]-A[i][j]
    print(*result[i])