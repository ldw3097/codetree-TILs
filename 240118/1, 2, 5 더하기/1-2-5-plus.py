n = int(input())
dp = [987654321] * (n+1)
dp[0] = 1

for i in range(1, n+1):
    ret = dp[i-1]
    ret += dp[i-2] if i>=2 else 0
    ret += dp[i-5] if i>=5 else 0
    dp[i] = ret% 10007
print(dp[n])