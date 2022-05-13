q = int(input())
yama = []
result = []
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        yama.insert(0, x)
    if t == 2:
        yama.append(x)
    if t == 3:
        result.append(yama[x-1])
print(*result, sep='\n')
