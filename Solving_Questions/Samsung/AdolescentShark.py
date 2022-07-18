# [청소년 상어]
# 난이도: 상
# 권장 풀이 시간: 50분
# 시간 제한: 1초
# 메모리 제한: 512MB

graph = [[None] * 4 for _ in range(4)]
for i in range(4):
  array = list(map(int, input().split()))
  for j in range(4):
    graph[i][j] = [array[j * 2], array[(j * 2) + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(graph, num):
  for i in range(4):
    for j in range(4):
      if graph[i][j][0] == num:
        return (i, j)
  return None

def turn_left(direction):
  return (direction + 1) % 8

# 물고기 이동 (상어 있으면 왼쪽으로 회전)
def move_fishes(graph, now_x, now_y):
  for i in range(17):
    location = find_fish(graph, i)
    if location != None:
      # 방향 회전하면서 이동 가능 확인
      direction = graph[location[0]][location[1]][1]
      for i in range(8):
        nx = location[0] + dx[direction]
        ny = location[1] + dy[direction]
        if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
          if not (nx == now_x and ny == now_y):
            graph[location[0]][location[1]][1] = direction
            graph[location[0]][location[1]], graph[nx][ny] = graph[nx][ny], graph[location[0]][location[1]]
            break
        direction = turn_left(direction)
  
# 상어가 이동할 수 있는 경우의 수
def move_shark_cases(graph, x, y):
  cases = []
  d = graph[x][y][1]
  for i in range(4):
    x += dx[d]
    y += dy[d]
    if 0 <= x and x < 4 and 0 <= y and y < 4:
      if graph[x][y][0] != -1:
        cases.append((x, y))
  return cases

result = 0
import copy 
# DFS (현재 물고기 먹음)
def DFS2(graph, x, y, total):
  global result
  graph = copy.deepcopy(graph)
  # 현재 상어 위치
  now_x = x
  now_y = y

  # 물고기 먹음
  total += graph[now_x][now_y][0]
  graph[now_x][now_y][0] = -1

  # 물고기 이동
  move_fishes(graph, x, y)

  # 상어가 갈 수 있는 경우의 수
  cases = move_shark_cases(graph, now_x, now_y)

  if len(cases) == 0:
    result = max(result, total)
    return 
  for case in cases:
    next_x, next_y = case
    DFS2(graph, next_x, next_y, total)
  
DFS2(graph, 0, 0, 0)
print(result)