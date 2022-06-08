import math

n, l = map(int, input().split())
dp = [0] * (n+1)
dp[0] = dp[1] = 1
for i in range(2, n+1):
    dp[i] += dp[i-1]
    if i-l >= 0:
        dp[i] += dp[i-l]
    dp[i] %= 10**9 + 7
print(dp[-1])