n = int(input())
a = [int(input()) for _ in range(n)]
a.insert(0, 0)
result = [1]
idx = 1
for i in range(n):
    result.append(a[idx])
    idx = a[idx]
print(result.index(2) if 2 in result else -1)