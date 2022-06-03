n, q = map(int, input().split())
x = [int(input()) for _ in range(q)]
# a[idx] = value
a = [i for i in range(1, n+1)]
# idx[value] = idx
idx = [i for i in range(n)]
for i in range(q):
    target_v = x[i]-1
    target_i = idx[target_v]
    next_i = target_i-1 if target_i == n-1 else target_i+1
    next_v = a[next_i]-1
    a[target_i], a[next_i] = a[next_i], a[target_i]
    idx[target_v], idx[next_v] = idx[next_v], idx[target_v]
print(*a)