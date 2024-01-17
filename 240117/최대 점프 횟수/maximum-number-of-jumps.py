import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
dp[0] = 1
for i in range(1,n):
    maxval = 0
    for j in range(i):
        if i-j <= arr[j] and arr[j] > 0:
            maxval = max(maxval, dp[j])
    dp[i] = maxval+1
print(max(dp)-1)