# [미로 탐색]
# 2178
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
  data = list(map(int, sys.stdin.readline().rstrip()))
  graph.append(data)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS(graph, start):
  q = deque([start])
  graph[start[0]][start[1]] = 2
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < m:
        if graph[nx][ny] == 1:
          q.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1

BFS(graph, (0,0))
print(graph[n-1][m-1] - 1)
      