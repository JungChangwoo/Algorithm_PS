# [케빈 베이컨의 6단계 법칙]
# 1389번
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
INF = int(1e9)

import heapq
def dikstra(start):
  global min_result, result
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q, (cost, i))
  total = 0
  # 케빈 베이컨 수 계산
  for i in range(1, len(distance)):
    total += distance[i]
  # 만약 케빈 베이컨 수가 가장 작다면
  if min_result > total:
    min_result = total
    result = start
    
min_result = INF
result = 0
for i in range(1, n+1):
  dikstra(i)
print(result)