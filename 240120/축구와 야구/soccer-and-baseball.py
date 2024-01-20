import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append( tuple(map(int, input().split())) )

dp = [[0]*10 for _ in range(12)]
dp[11][9] = (0, arr)

for i in range(9, -1, -1):
    for j in range(11, -1, -1):
        if (j,i) == (11,9):
            continue
        news1 = news2 = -1
        if j < 11:
            s1, arr1 = dp[j+1][i]
            maxval1 = max(arr1, key=lambda x: (x[0], -x[1]))
            news1 = s1 + maxval1[0]
        if i < 9:
            s2, arr2 = dp[j][i+1]
            maxval2 = max(arr2, key=lambda x: (x[1], -x[0]))
            news2 = s2 + maxval2[1]

        if news1 > news2:
            newarr = arr1.copy()
            newarr.remove(maxval1)
            dp[j][i] = (news1,newarr)
        else:
            newarr = arr2.copy()
            newarr.remove(maxval2)
            dp[j][i] = (news2, newarr)

print(dp[0][0][0])