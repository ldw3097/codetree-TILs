import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )
dp = [[-1]*n for i in range(n)]

dy = (1,-1,0,0)
dx = (0,0,1,-1)
def traverse(visited, y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    ret = 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<n and arr[ny][nx] > arr[y][x] and (ny,nx) not in visited:
            newvisited = visited.copy()
            newvisited.add((ny, nx))
            ret = max(ret, traverse(newvisited, ny, nx)+1 )
    dp[y][x] = ret
    return ret

ret = 0
for i in range(n):
    for j in range(n):
        ret = max(ret, traverse(set(), i, j))
print(ret)