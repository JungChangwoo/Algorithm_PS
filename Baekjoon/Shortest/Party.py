# [파티]

import sys
n, m, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (n+1)

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

result = [0] * (n+1)
for i in range(1, n+1):
  distance = [INF] * (n+1)
  dikstra(i)
  result[i] = distance[x]

distance = [INF] * (n+1)
dikstra(x)
for i in range(1, n+1):
  result[i] += distance[i]

print(max(result))