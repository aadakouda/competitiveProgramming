n, x = map(int, input().split())
alc = 0
result = -1
for i in range(n):
    v, p = map(int, input().split())
    alc += v*p
    if alc > x*100:
        result = i + 1
        break
print(result)
