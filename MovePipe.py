# [파이프 옮기기 1]
# 17070번
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))


dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
dx = [0, 1, 1]
dy = [1, 1, 0]

def DFS(x, y, type):
  global result
  if x == n-1 and y == n-1:
    return 1
  if dp[x][y][type] > 0:
    return dp[x][y][type]
  for d in range(3):
    nx = x + dx[d]
    ny = y + dy[d]
    if (type == 0 and d == 2) or (type == 2 and d == 0):
      continue
    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 0:
        if d == 1:
          if graph[x][y+1] == 1 or graph[x+1][y] == 1:
            continue
        dp[x][y][type] += DFS(nx, ny, d)
  return dp[x][y][type]

if graph[n-1][n-1] == 1:
  print(0)
else:
  DFS(0, 1, 0)
  print(dp[0][1][0])