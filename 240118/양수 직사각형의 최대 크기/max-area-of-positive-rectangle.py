import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

ret = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] < 0:
            continue
        width = m-j
        for k in range(i, n):
            for l in range(j, j+width):
                if arr[k][l] <= 0:
                    width = l-j
                    break
            if width == 0:
                break
            ret = max(ret, (width)*(k-i+1))

print(ret)