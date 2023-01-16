# [도넛 행성]
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, n, m):
  q = deque([(x, y)])
  graph[x][y] = 2
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if nx == -1:
        nx = n - 1
      elif nx == n:
        nx = 0
      if ny == -1:
        ny = m - 1
      elif ny == m:
        ny = 0
      if graph[nx][ny] == 0:
        q.append((nx, ny))
        graph[nx][ny] = 2
        
result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      result += 1
      BFS(i, j, n, m)
print(result)