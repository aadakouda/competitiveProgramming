n = int(input())
a = [[] for _ in range(n)]
a[0] = ['1']
for i in range(1, n):
    for j in range(i+1):
        if j == 0 or j == i:
            a[i].append('1')
        else:
            a[i].append(str(int(a[i-1][j-1]) + int(a[i-1][j])))
for i in range(n):
    print(*a[i])