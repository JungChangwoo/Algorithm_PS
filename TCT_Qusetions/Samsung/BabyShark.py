# [아기 상어]
# 난이도: 중상
# 권장 풀이 시간: 50분
# 시간 제한: 2초
# 메모리 제한: 512MB

n = int(input())
graph = []

for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  
# 상화좌우 벡터
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

shark = (0, 0)
sharkSize = 2

# 처음 상어 위치 찾기
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      shark = (i, j)
      graph[i][j] = 0

# 먹이 찾기
from collections import deque
def find_fish(graph, start, visited):
  q = deque([start])
  visited[start[0]][start[1]] = True
  while q:
    x, y = q.popleft()
    result = []
    # 상하좌우 이동
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
      if graph[nx][ny] > sharkSize:
        continue
      if visited[nx][ny]:
        continue
      if 1 <= graph[nx][ny] < sharkSize:
        result.append((nx, ny))
      x = nx
      y = ny
      visited[x][y] = True
      q.append((x, y))
    # 물고기 확인
    if len(result) == 1:
      return result[0]
    elif len(result) >=2:
      result.sort()
      return result[0]
  return (-1, -1)
  
count = 0
eat = 0
while True:
  visited = [[False for _ in range(n)] for _ in range(n)]
  x, y = find_fish(graph, shark, visited)
  if x == -1:
    break
  count += abs((shark[0] - x)) + abs((shark[1] - y))
  eat += 1
  if sharkSize == eat:
    sharkSize += 1
    eat = 0
  graph[x][y] = 0
  shark = (x, y)

print(count)
###################################################################
# 이코테 답
from collections import deque
INF = int(1e9)

n = int(input())

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
  for j in range(n):
    if array[i][j] == 9:
      now_x, now_y = i, j
      array[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
  dist = [[-1] * n for _ in range(n)]
  dist[now_x][now_y] = 0
  q = deque([(now_x, now_y)])
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))
  return dist

def find(dist):
  x, y = 0, 0
  min_dist = INF
  # 가장 위부터 왼쪽부터 찾음
  for i in range(n):
    for j in range(n): # 갈 수 있고 먹을 수 있으며 물고기여야함
      if dist[i][j] != -1 and array[i][j] < now_size and 1 <= array[i][j]:
        if dist[i][j] < min_dist:
          min_dist = dist[i][j]
          x, y = i, j
  if min_dist == INF:
    return None
  else:
    return x, y, min_dist

result = 0
ate = 0
while True:
  value = find(bfs())
  if value == None:
    print(result)
    break;
  else:
    now_x, now_y = value[0], value[1]
    result += value[2]
    array[now_x][now_y] = 0
    ate += 1
    if ate == now_size:
      now_size += 1
      ate = 0
  
  
