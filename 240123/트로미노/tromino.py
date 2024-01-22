import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )

blocks = (((0,1), (0,2)), ((1,0), (2,0)), ((1,0), (1,1)), ((0,1), (1,0)), ((1,0), (1,-1)), ((0,1), (1,1))   )

def placeblock(block, y, x):
    ret = arr[y][x]
    for dy, dx in block:
        ny,nx = y+dy, x+dx
        if 0>ny or n <=ny or 0>nx or m <= nx:
            return -1
        ret += arr[ny][nx]
    return ret

ret = -1
for i in range(n):
    for j in range(m):
        for block in blocks:
            ret = max(ret, placeblock(block, i, j))
print(ret)