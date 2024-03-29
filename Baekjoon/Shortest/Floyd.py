# [플로이드]
# 11404번
import sys
INF = int(1e9)
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))

import heapq
def dikstra(start):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  return distance

for i in range(1, n+1):
  d = dikstra(i)
  for j in range(1, n+1):
    if d[j] == INF:
      print(0, end=' ')
    else:
      print(d[j], end=' ')
  print()