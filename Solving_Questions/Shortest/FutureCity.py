# [전보] Chapter 2
# 난이도: 최상
# 권장 풀이 시간: 60분
# 시간 제한: 1초

n, m, c = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
for i in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((z, y))
print(graph)

distance = [INF] * (n+1)

import heapq
def dikstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost, v = i
      cost = cost + dist
      if cost < distance[v]:
        distance[v] = cost
        heapq.heappush(q, (cost, v))

dikstra(c)
count = 0
time = 0
for i in range(1, len(distance)):
  if distance[i] != INF:
    count += 1
    time = max(distance[i], time)
print(count - 1, time)
# 일방향
# C에서 출발하여 도착 가능한 도시의 개수
# C에서 출발하여 모든 도시가 메세지를 받는 데 까지 걸리는 시간
# => 마지막에 모든 도시를 돌면서 가장 오래 걸린 