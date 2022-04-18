n = int(input())
s = input()
atcoder = 'atcoder'
dp = [[0] * 8 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    for j in range(8):
        if j < 7 and s[i] == atcoder[j]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= 10**9+7
print(dp[-1][-1])