import sys
input = sys.stdin.readline
from collections import *
import heapq
n, m = map(int, input().split())

connect = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    connect[a].append((b,c))
    connect[b].append((a,c))

hq = [(0,n)] 
adj = [98765321]*(n+1)
adj[0] = 0
adj[n] = 0
visited = set()
while hq:
    val, node = heapq.heappop(hq)
    if node in visited:
        continue
    visited.add(node)
    for b, c in connect[node]:
        if adj[b] > val + c:
            adj[b] = val+c 
            heapq.heappush(hq, (val+c, b))
print(max(adj))