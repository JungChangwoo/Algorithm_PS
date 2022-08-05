# 청소년 상어
# 19236번

graph = [[None] * 4 for _ in range(4)]
for i in range(4):
  data = list(map(int, input().split()))
  for j in range(4):
    graph[i][j] = [data[j * 2], data[(j * 2) + 1] - 1]
# 상, 상좌, 좌, 좌하, 하, 우하, 우, 우상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(d):
  d += 1
  if d == 8:
    return 0
  return d
  
def find_fish(graph, index):
  for i in range(4):
    for j in range(4):
      if graph[i][j][0] == index:
        return (i, j, graph[i][j][1])
  return None

def fish_move(graph):
  # 작은 순서대로 이동
  for index in range(1, 17):
    findResult = find_fish(graph, index)
    if findResult == None:
      continue
    x, y, d = findResult
    for i in range(8):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
        # 상어가 아니라면
        if graph[nx][ny][0] != -1:
          graph[x][y][1] = d
          graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
          break
      d = turn_left(d)
          
def getCases(graph, shark, d):
  cases = []
  x, y = shark
  for i in range(4):
    x += dx[d]
    y += dy[d]
    if 0 <= x and x < 4 and 0 <= y and y < 4:
      # 물고기가 존재하는 경우
      if 1 <= graph[x][y][0] and graph[x][y][0] <= 16:
        cases.append((x, y))
  if len(cases) == 0:
    return None
  else:
    return cases


import copy
result = 0
def AdolescentShark(graph, shark, total):
  global result
  graph = copy.deepcopy(graph)
  total += graph[shark[0]][shark[1]][0]
  graph[shark[0]][shark[1]][0] = -1
  direction = graph[shark[0]][shark[1]][1]
  fish_move(graph)
  cases = getCases(graph, shark, direction)
  
  if cases == None:
    result = max(result, total)
    return
    
  graph[shark[0]][shark[1]][0] = 0
  for case in cases:
    AdolescentShark(graph, case, total)
  
AdolescentShark(graph, (0,0), 0)
print(result)
