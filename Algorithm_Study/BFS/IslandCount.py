# [섬의 개수]
# 4963번
import sys
from collections import deque
def bfs(graph, x, y, w, h):
  q = deque()
  q.append((x, y))
  graph[x][y] = 2
  while q:
    x, y = q.popleft()
    
    for d in range(9):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < h and 0 <= ny < w:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 2
          q.append((nx, ny))

# 제자리, 상, 하, 좌, 우, 상우, 하우, 하좌, 상좌
dx = [0, -1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 0, -1, 1, 1, 1, -1, -1]

while True:
  w, h = map(int, sys.stdin.readline().split())
  if w == 0 and h == 0:
    break
    
  graph = []
  for i in range(h):
    graph.append(list(map(int, sys.stdin.readline().split())))

  result = 0
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(graph, i, j, w, h)
        result += 1
  print(result)
