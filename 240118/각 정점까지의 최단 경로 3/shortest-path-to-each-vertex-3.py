import sys
input = sys.stdin.readline
from collections import *
import heapq
n, m = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    a, b ,c = map(int, input().split())
    dic[a].append((b,c))
inf = 987654321
dist = [inf]*(n+1)
dist[1] = 0
hq = [(0,1)]
visited = set()
while hq:
    val, num = heapq.heappop(hq)
    if num in visited:
        continue
    visited.add(num)
    for adj, length in dic[num]:
        if length + val < dist[adj]:
            dist[adj] = length +val
            heapq.heappush(hq, (dist[adj], adj))
for i in range(2, n+1):
    if dist[i] == inf:
        print(-1)
    else:
        print(dist[i])