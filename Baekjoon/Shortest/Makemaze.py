# [미로만들기]
# 2665번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))
INF = int(1e9)
distance = [[INF] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS():
  q = deque()
  q.append((0, 0, 0))
  distance[0][0] = 0
  while q:
    dist, x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        cost = dist
        # 검은방 아라면
        if graph[nx][ny] == 0:
          cost += 1
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          q.append((cost, nx, ny))

import heapq
def dikstra():
  q = []
  heapq.heappush(q, (0, 0, 0))
  distance[0][0] = 0
  while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
      continue
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        cost = dist
        if graph[nx][ny] == 0:
          cost += 1
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))

#BFS()
dikstra()
print(distance[n-1][n-1])
  