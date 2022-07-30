# [숨바꼭질 3]
# 13549번
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
graph = [[] for _ in range(100001)]
for i in range(100000):
  if i-1 >= 0:
    graph[i].append((i-1, 1))
  if i+1 <= 100000:
    graph[i].append((i+1, 1))
  if i*2 <= 100000:
    graph[i].append((i*2, 0))
distance = [INF] * 100001

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

dikstra(n)
print(distance[k])
  