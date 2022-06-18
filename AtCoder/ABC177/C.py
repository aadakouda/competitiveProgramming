n = int(input())
a = list(map(int, input().split()))
asum = [a[0]]
for i in range(1, n):
    asum.append(asum[-1]+a[i])
mod = 10**9 + 7
result = 0
for i in range(n-1):
    result += a[i] * (asum[-1]-asum[i])
print(result % mod)