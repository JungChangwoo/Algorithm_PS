# [최소비용 구하기]

import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (n+1)

start, end = map(int, sys.stdin.readline().rstrip().split())

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
print(distance[end])
      