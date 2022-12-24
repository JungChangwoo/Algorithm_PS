# [사탕 게임]
# 3085번
import sys
n = int(sys.stdin.readline().rstrip())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def get_xcount():
  global result 
  for i in range(n):
    value = 1
    for j in range(1, n):
      if graph[i][j] == graph[i][j-1]:
        value += 1
      else:
        value = 1
      result = max(result, value)

def get_ycount():
  global result
  for j in range(n):
    value = 1
    for i in range(1, n):
      if graph[i][j] == graph[i-1][j]:
        value += 1
      else:
        value = 1
      result = max(result, value)

for x in range(n):
  for y in range(n):
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[x][y] != graph[nx][ny]:
          graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
          get_xcount()
          get_ycount()
          graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
print(result)
    