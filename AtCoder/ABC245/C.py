n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lst = []
for i in range(n):
    lst.append([A[i], B[i]])
dp = [[False] * 2 for _ in range(n)]
dp[0] = [True, True]
for i in range(n-1):
    for j in range(2):
        if dp[i][j]:
            if abs(lst[i][j] - lst[i+1][j]) <= k:
                dp[i+1][j] = True
            if abs(lst[i][j] - lst[i+1][(j+1)%2]) <= k:
                dp[i+1][(j+1)%2] = True
print('Yes' if any(dp[-1]) else 'No')