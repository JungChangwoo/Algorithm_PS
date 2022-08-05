# [아기 상어]
# 16236번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark = (0, 0)
sharkSize = 2
eat = 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      shark = (i, j)
      graph[i][j] = 0

def findFish(dist):
  x, y = 0, 0
  min_dist = int(1e9)
  for i in range(n):
    for j in range(n):
      if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < sharkSize:
        if dist[i][j] < min_dist:
          x, y = i, j
          min_dist = dist[i][j]
  if min_dist == int(1e9):
    return None
  else:
    return x, y, min_dist
  
from collections import deque
def move():
  global shark
  global sharkSize
  dist = [[-1] * n for _ in range(n)]
  x, y = shark
  q = deque()
  q.append((x, y))
  dist[x][y] = 0
  while q:
    x, y = q.popleft()
    # 상, 하, 좌, 우
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위에 벗어나는지 확인
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        # 방문 했는지 and 상어사이즈보다 작거나 같은지
        if dist[nx][ny] == -1 and graph[nx][ny] <= sharkSize:
          q.append((nx, ny))
          dist[nx][ny] = dist[x][y] + 1
  return dist
  
result = 0
while True:
  moveResult = findFish(move())
  if moveResult == None:
    break
  else:
    x, y, distance = moveResult
  shark = (x, y)
  result += distance
  graph[x][y] = 0
  eat += 1
  if sharkSize == eat:
    sharkSize += 1
    eat = 0

print(result)

# 상어위치
# 상어 사이즈
# 물고기 먹은 횟수
# move 함수 (BFS 탐색 => 물고기면 array에 담아줌 -1 => 물고기 찾기 함수에 넘겨줌(copy, array))
# 물고기 찾는 함수 (i, j)

