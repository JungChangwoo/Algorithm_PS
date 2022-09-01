# [알파벳]
# 1987번
import sys
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
visited = [[False] * m for _ in range(n)]
paths = [0] * 26

from collections import deque
def DFS(count, x, y):
  global result
  isEnd = True
  # 상, 하, 좌, 우
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
      if not visited[nx][ny] and paths[ord(graph[nx][ny]) - 65] == 0:
        isEnd = False
        visited[nx][ny] = True
        paths[ord(graph[nx][ny]) - 65] = 1
        DFS(count + 1, nx, ny)
        visited[nx][ny] = False
        paths[ord(graph[nx][ny]) - 65] = 0
  if isEnd:
    result = max(result, count)
    
result = 0
visited[0][0] = True
paths[ord(graph[0][0]) - 65] = 1
DFS(1, 0, 0)
print(result)