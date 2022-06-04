n, m, k = map(int, input().split())
s = 998244353
cnt = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, m+1):
    cnt[1][i] = 1
for a in range(2, n+1):
    cnt2 = cnt[a-1][:]
    for i in range(1, k+1):
        cnt2[i] += cnt2[i-1]
    for b in range(1, k+1):
        cnt[a][b] = cnt2[b-1]-cnt2[max(0, b-m-1)]
print(sum(cnt[n]) % s)