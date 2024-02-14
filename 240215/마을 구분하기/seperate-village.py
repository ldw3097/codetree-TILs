n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ret = []
def traverse(y,x):
    arr[y][x] = 0
    ret = 1
    for dy,dx in zip((1,-1,0,0),(0,0,1,-1)):
        ny,nx = y+dy,x+dx
        if 0<=ny<n and 0<=nx<n and arr[ny][nx]==1:
            ret += traverse(ny,nx)
    return ret

for y in range(n):
    for x in range(n):
        if arr[y][x]==1:
            ret.append(traverse(y,x))
ret.sort()
print(len(ret))
for i in ret:
    print(i)