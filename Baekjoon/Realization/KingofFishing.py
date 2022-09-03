# [낚시왕]
# 17143번
import sys
r, c, m = map(int, sys.stdin.readline().split())
graph = [[0] * c for _ in range(r)]
sharks = [[] for _ in range(10001)]
# 상, 하, 우, 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(m):
  x, y, s, d, z = map(int, sys.stdin.readline().split())
  graph[x-1][y-1] = z
  sharks[z].append(s)
  sharks[z].append(d-1)
def get_dir(d):
  if d == 0:
    return 1
  if d == 1:
    return 0
  if d == 2:
    return 3
  if d == 3:
    return 2

def move(new_graph, x, y, size):
  dir = sharks[size][1]
  speed = sharks[size][0]
  for i in range(speed):
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 만약, 끝에 도착하면 반대로
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      dir = get_dir(dir)
      nx = x + dx[dir]
      ny = y + dy[dir]
    x, y = nx, ny
  # 만약, 도착한 지점에 상어가 있다면
  if new_graph[x][y] != 0:
    new_graph[x][y] = max(new_graph[x][y], size)
  else:
    new_graph[x][y] = size
  # 상어 방향 바꿔주기
  sharks[size][1] = dir

def move_sharks():
  new_graph = [[0] * c for _ in range(r)]
  for i in range(r):
    for j in range(c):
      if graph[i][j] != 0:
        move(new_graph, i, j, graph[i][j])
  return new_graph

result = 0
# 낚시왕이 오른쪽으로 한 칸씩 이동
for j in range(c):
  # 제일 땅과 가까운 상어를 잡는다.
  for i in range(r):
    if graph[i][j] != 0:
      result += graph[i][j]
      graph[i][j] = 0
      break
  # 상어가 이동한다.
  new_graph = move_sharks()
  graph = new_graph
  
print(result)