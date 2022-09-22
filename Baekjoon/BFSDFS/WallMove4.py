# [벽 부수고 이동하기 4]
# 16946번
import sys
import copy
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(area_graph, x, y, group):
  count = 1
  q = deque()
  q.append((x, y))
  area_graph[x][y] = group
  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < m:
        if area_graph[nx][ny] == 0:
          area_graph[nx][ny] = group
          q.append((nx, ny))
          count += 1
  return count
          
# 영역을 구한다.
area = []
group = 2
area_graph = copy.deepcopy(graph)
for i in range(n):
  for j in range(m):
    if area_graph[i][j] == 0:
      count = BFS(area_graph, i, j, group)
      area.append(count)
      group += 1

def get_count(x, y):
  count = 0
  visited = []
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
      group = area_graph[nx][ny]
      if area_graph[nx][ny] >= 2 and group not in visited:
        count += area[group - 2]
        visited.append(group)
  return count
        
      
# 전체 지도를 탐색한다.
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      graph[i][j] = (get_count(i, j) + 1) % 10

for i in range(n):
  for j in range(m):
    print(graph[i][j], end='')
  print()
      
      