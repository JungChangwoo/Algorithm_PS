# [피리부는 사나이]
# 16724번
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  data = list(sys.stdin.readline().rstrip())
  for i in range(len(data)):
    if data[i] == 'U':
      data[i] = 0
    elif data[i] == 'D':
      data[i] = 1
    elif data[i] == 'L':
      data[i] = 2
    else:
      data[i] = 3
  graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y, nowGroup):
  q = deque()
  q.append((x, y))
  visited[x][y] = nowGroup

  while q:
    x, y = q.popleft()
    d = graph[x][y]
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
      if visited[nx][ny] != nowGroup: # 현재 Group이 아닐경우
        if visited[nx][ny] != 0: # 만약, 다른 그룹과 만났다면
          return True
        else: # 다릅 그룹과 만나지 않으면서 방문하지 않은 곳이라면
          q.append((nx, ny))
          visited[nx][ny] = nowGroup

  return False
  
result = 0
visited = [[0] * m for _ in range(n)]
group = 1
for i in range(n):
  for j in range(m):
    if not visited[i][j]:
      isCrossGroup = BFS(i, j, group)
      group += 1
      if not isCrossGroup:
        result += 1
print(result)