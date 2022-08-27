# [토마토]
# 7569번
import sys
m, n, h = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(h)]
for i in range(h):
  for _ in range(n):
    graph[i].append(list(map(int, sys.stdin.readline().split())))

# [상, 하, 좌, 우, 위, 아래]
move = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]

from collections import deque
def BFS(m, n, h):
  q = deque()
  # 처음에 익은 토마토를 q에 담는다.
  for k in range(h):
    for i in range(n):
      for j in range(m):
        if graph[k][i][j] == 1:
          q.append((0, k, i, j))
  value = 0
  while q:
    count, now_h, x, y = q.popleft()
    # 상, 하, 좌, 우, 위, 아래
    for i in range(6):
      nh = now_h + move[i][0]
      nx = x + move[i][1]
      ny = y + move[i][2]
      if 0 <= nx < n and 0 <= ny < m and 0 <= nh < h: 
        if graph[nh][nx][ny] == 0:
          graph[nh][nx][ny] = 1
          q.append((count + 1, nh, nx, ny))
          value = count + 1
    
  return value

result = BFS(m, n, h)
success = True
# 안 익은 토마토가 있는지 확인
for k in range(h):
  for i in range(n):
    for j in range(m):
      if graph[k][i][j] == 0:
        success = False
        break
if success:
  print(result)
else:
  print(-1)
