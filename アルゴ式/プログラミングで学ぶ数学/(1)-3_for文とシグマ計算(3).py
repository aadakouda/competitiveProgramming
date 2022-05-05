# https://algo-method.com/tasks/568

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(m):
        result += a[i]+b[j]

print(result)
