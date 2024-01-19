import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append( list(map(int, input().split())) )

def traverse(y, x, val):
    if arr[y][x] != val:
        return 0
    arr[y][x] = -1
    ret = 1
    for dy, dx in zip((1,-1,0,0), (0,0,1,-1)):
        ny = y+dy
        nx = x+dx 
        if 0<= ny <n and 0<=nx<n:
            ret += traverse(ny,nx,val)
    return ret

blast = 0
biggest = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != -1:
            block = traverse(i,j,arr[i][j])
            if block >= 4:
                blast += 1
            biggest = max(biggest, block)
print(blast, biggest)