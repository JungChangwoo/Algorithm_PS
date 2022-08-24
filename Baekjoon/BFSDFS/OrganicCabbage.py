# [유기농 배추]
# 1012번

import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque
def BFS(x, y):
  q = deque()
  q.append((x, y))
  graph[x][y] = 2
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 2
          q.append((nx, ny))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  m, n, k = map(int, sys.stdin.readline().rstrip().split())
  graph = [[0] * m for _ in range(n)]
  for _ in range(k):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1

  result = 0
  # 만약 배추가 있다면
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        BFS(i, j)
        result += 1
  print(result)