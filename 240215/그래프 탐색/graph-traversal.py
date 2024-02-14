from collections import *

n, m = map(int, input().split())
df = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    df[a].append(b)
    df[b].append(a)

def traverse(pos, visited):
    ret = 1
    for npos in df[pos]:
        if npos not in visited:
            visited.add(npos)
            ret += traverse(npos, visited)
    return ret

ret = traverse(1, {1,}) -1
print(ret)