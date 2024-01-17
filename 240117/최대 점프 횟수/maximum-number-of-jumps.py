import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0]*n
for i in range(1,n):
    maxval = 0
    for j in range(i):
        if i-j <= arr[j]:
            maxval = max(maxval, dp[j])
    dp[i] = maxval+1
print(max(dp))