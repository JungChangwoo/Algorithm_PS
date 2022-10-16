# [적록색약]
# 10026번
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, colors):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny] and graph[nx][ny] in colors:
          visited[nx][ny] = True
          q.append((nx, ny))
          
visited = [[False] * n for _ in range(n)]
normal_result = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      BFS(i, j, [graph[i][j]])
      normal_result += 1
      
visited = [[False] * n for _ in range(n)]
weakness_result = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      if graph[i][j] == 'B':
        BFS(i, j, [graph[i][j]])
      else:
        BFS(i, j, ['R', 'G'])
      weakness_result += 1
print(normal_result, weakness_result)