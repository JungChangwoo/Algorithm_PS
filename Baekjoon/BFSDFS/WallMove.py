# [벽 부수고 이동하기]
# 2206번
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS(new_graph, x, y, wall):
  q = deque()
  q.append((x, y, wall))
  new_graph[x][y][wall] = 1
  while q:
    x, y, wall = q.popleft()
    if x == n-1 and y == m-1:
      return new_graph[x][y][wall]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny][wall] == 0:
        # 벽이고 벽을 뚫을 수 있다면
        if graph[nx][ny] == 1 and wall == 0:
            new_graph[nx][ny][1] = new_graph[x][y][wall] + 1
            q.append((nx, ny, 1))
        # 벽이 아니라면
        elif graph[nx][ny] == 0:
          new_graph[nx][ny][wall] = new_graph[x][y][wall] + 1
          q.append((nx, ny, wall))
  return -1

INF = int(1e9)
result = INF
new_graph = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(BFS(new_graph, 0, 0, 0))