# [서강그라운드]
# 14938번
import sys
n, m, r = map(int, sys.stdin.readline().rstrip().split())
items = list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] * n for _ in range(n)]
for i in range(r):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  graph[a-1].append((c, b-1))
  graph[b-1].append((c, a-1))
  
INF = int(1e9)

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
      cost = i[0] + dist
      if cost < distance[i[1]]:
        distance[i[1]] = cost
        heapq.heappush(q, (cost, i[1]))

result = 0
for i in range(n):
  distance = [INF] * n
  dikstra(i)
  # 각 정점을 돌면서 m보다 작거나 같은지
  total = 0
  for j in range(len(distance)):
    if distance[j] != INF and distance[j] <= m:
      total += items[j]
  result = max(result, total)
print(result)

# 시작으로부터 모든 정점까지의 최단 거리를 구함
# 수색범위보다 작거나 같으면 더함