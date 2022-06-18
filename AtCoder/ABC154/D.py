n, k = map(int, input().split())
p = list(map(int, input().split()))
pk = [(1+p[0]) * p[0] / 2 / p[0]]
for i in range(1, n):
    pk.append(pk[-1] + (1+p[i])*p[i] / 2 / p[i])
ma = pk[k-1]
for i in range(n-k):
    ma = max(ma, pk[i+k] - pk[i])
print(ma)