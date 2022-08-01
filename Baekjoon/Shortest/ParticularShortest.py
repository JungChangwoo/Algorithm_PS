# [특정한 최단 경로]
# 1504번
import sys
n, e = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for i in range(e):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
INF = int(1e9)
v1, v2 = map(int, sys.stdin.readline().rstrip().split())

import heapq
def dikstra(start, end):
  d = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  d[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > d[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < d[i[0]]:
        d[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return d[end]
  
pathA = dikstra(1, v1) + dikstra(v1, v2) + dikstra(v2, n)
pathB = dikstra(1, v2) + dikstra(v2, v1) + dikstra(v1, n)

result = min(pathA, pathB)
if result >= INF:
  print(-1)
else:
  print(result)