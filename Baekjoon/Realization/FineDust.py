# [미세먼지 안녕!]
# 17144번

# 1. 미세먼지 graph에 퍼뜨린후 자신의 양을 줄인다.
# 2. 미세먼지 graph에 있는 값만큼 추가적으로 채워준다.
# 3. 공기청정기 돌린다.
import sys
r, c, t = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
  graph.append(list(map(int, sys.stdin.readline().split())))

cleaner1 = 0
cleaner2 = 0
for i in range(r):
  if graph[i][0] == -1:
    cleaner1 = i
    cleaner2 = i + 1
    break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread(x, y, dust):
  value = graph[x][y] // 5
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < r and 0 <= ny < c:
      if graph[nx][ny] != -1:
        dust[nx][ny] += value
        graph[x][y] -= value

def moveDust():
  dust = [[0] * c for _ in range(r)]
  for i in range(r):
    for j in range(c):
      if graph[i][j] > 0:
        spread(i, j, dust)
  for i in range(r):
    for j in range(c):
      if dust[i][j] > 0:
        graph[i][j] += dust[i][j]

def clean_up(x, y):
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  prev = 0
  for d in range(4):
    while True:
      nx = x + dx[d]
      ny = y + dy[d]
      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        break
      if graph[nx][ny] == -1:
        break
      graph[nx][ny], prev = prev, graph[nx][ny]
      x, y = nx, ny

def clean_down(x, y):
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  prev = 0
  for d in range(4):
    while True:
      nx = x + dx[d]
      ny = y + dy[d]
      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        break
      if graph[nx][ny] == -1:
        break
      graph[nx][ny], prev = prev, graph[nx][ny]
      x, y = nx, ny

for _ in range(t):
  moveDust()
  clean_up(cleaner1, 0)
  clean_down(cleaner2, 0)

result = 0
for i in range(r):
  for j in range(c):
    if graph[i][j] != -1:
      result += graph[i][j]
print(result)