n = int(input())
dp = [1]*9
for i in range(n-1):
    dp_temp = [0]*9
    for j in range(9):
        dp_temp[j] += dp[j]
        if j > 0:
            dp_temp[j-1] += dp[j]
        if j < 8:
            dp_temp[j+1] += dp[j]
        dp_temp[j] %= 998244353
    dp = dp_temp
print(sum(dp)%998244353)