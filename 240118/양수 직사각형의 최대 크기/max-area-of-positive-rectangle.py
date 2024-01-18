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
        parret = 0
        width = m-j
        for k in range(i, n):
            parwidth = 0
            for l in range(j, j+width):
                if arr[k][l] > 0:
                    parwidth += 1
                else:
                    width = parwidth
                    break
                parret = max(parret, (width)*(k-i+1))
            if width == 0:
                break
        ret = max(ret, parret)
print(ret)