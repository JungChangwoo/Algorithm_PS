# [토마토]
# 7576번

import sys
m, n = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS():
  q = deque()
  # 처음에 익은 토마토를 모두 담는다.
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        q.append((0, i, j))
  value = 0
  while q:
    count, x, y = q.popleft()
    # 상하좌우
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          q.append((count + 1, nx, ny))
          value = count + 1
  return value

result = BFS()
success = True
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      success = False
      break
if success:
  print(result)
else:
  print(-1)
          