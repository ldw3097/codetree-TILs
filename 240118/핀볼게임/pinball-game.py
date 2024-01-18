import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append( list(map(int, input().split()))  )

def mirror1(dy,dx):
    return (-dx, -dy)

def mirror2(dy,dx):
    return (dx, dy)


def move(y,x,direct):
    if arr[y][x] == 1:
        direct = mirror1(*direct)
    elif arr[y][x] == 2:
        direct= mirror2(*direct)
    return (y+direct[0] , x+direct[1], direct)


def game(y, x, direct):
    ret = 1
    while 0<=y<n and 0<=x<n:
        y,x,direct= move(y,x,direct)
        ret += 1
    return ret

ret = 0
for i in range(n):
    a = game(0, i, (1,0))
    b = game(n-1, i,(-1,0))
    c = game(i,0, (0,1))
    d = game(i,n-1, (0,-1))
    ret = max(ret, a, b, c, d)
print(ret)