# [나이트의 이동]
# 7562번
import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(graph, x, y, tx, ty, n):
  q = deque([(x, y, 0)])

  while q:
    x, y, count = q.popleft()

    if x == tx and y == ty:
      return count
      
    for d in range(8):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          q.append((nx, ny, count + 1))
          
  return -1

for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  graph = [[0] * n for _ in range(n)]
  x, y = map(int, sys.stdin.readline().split())
  tx, ty = map(int, sys.stdin.readline().split())

  print(bfs(graph, x, y, tx, ty, n))

# 1. pop
# 2. 일치 확인
# 3. 맞다면 -> return, 아니라면 -> 이동 후 append
  