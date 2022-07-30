# [최단경로]
# 1753번

import sys
v, e = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
INF = int(1e9)
graph = [[] for _ in range(v+1)]
for i in range(e):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

distance = [INF] * (v + 1)

import heapq
def dikstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dikstra(start)
for i in range(1, v+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])