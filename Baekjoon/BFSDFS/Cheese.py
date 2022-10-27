# 치즈
# 2638번
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
  q = deque()
  q.append((0, 0))
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
          if graph[nx][ny] == 1:
            count[nx][ny] += 1
          else:
            visited[nx][ny] = True
            q.append((nx, ny))

def AllRemove():
  for i in range(n):
    for j in range(m):
      if count[i][j] >= 2:
        graph[i][j] = 0

def isFinal():
  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0:
        return False
  return True

result = 0
while True:
  visited = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)]
  BFS()
  AllRemove()
  isEnd = isFinal()
  result += 1
  if isEnd:
    print(result)
    break
  
