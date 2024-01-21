a = input()
b = input()

dp = [[-1]*len(a) for _ in range(len(b))]
if a[0] == b[0]:
    dp[0][0] = 1
else:
    dp[0][0] = 2
for i in range(1,len(a)):
    if a[i] == b[0]:
        dp[0][i] = i
    else:
        dp[0][i] = dp[0][i-1]+1
for j in range(1, len(b)):
    if a[0] == b[j]:
        dp[j][0] = j
    else:
        dp[j][0] = dp[j-1][0]+1

for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1)
print(dp[len(b)-1][len(a)-1])