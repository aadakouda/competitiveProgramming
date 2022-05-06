# https://algo-method.com/tasks/579

n = int(input())
a = list(map(int, input().split()))
result = 1

for i in range(n):
    result *= a[i]
    result %= 10

print(result)
