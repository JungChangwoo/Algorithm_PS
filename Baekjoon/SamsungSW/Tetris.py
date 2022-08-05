# [테트로미노]
# 14500번
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

max_sum = 0
def DFS(x, y, count, sum):
  global max_sum
  if count == 3:
    max_sum = max(max_sum, sum)
    return 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if visited[nx][ny] == False:
        if count == 1:
          visited[nx][ny] = True
          DFS(x, y, count + 1, sum + graph[nx][ny])
          visited[nx][ny] = False
        visited[nx][ny] = True 
        DFS(nx, ny, count + 1, sum + graph[nx][ny])
        visited[nx][ny] = False
        
for i in range(n):
  for j in range(m):
    visited[i][j] = True
    DFS(i, j, 0, graph[i][j])
    visited[i][j] = False

print(max_sum)
    