# [청소년 상어]
# 난이도: 상
# 권장 풀이 시간: 50분
# 시간 제한: 1초
# 메모리 제한: 512MB

graph = [[(0, 0)] * 4 for _ in range(4)]
for i in range(4):
  array = list(map(int, input().split()))
  for j in range(4):
    graph[i][j] = (array[j * 2], array[(j * 2) + 1])

now_x, now_y = 0, 0
now_d = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 처음 상어 이동
result = 0
value = graph[0][0]
result += value[0]
now_d = value[1]
graph[0][0] = -1

# 회전
def rotate(d):
  if d == 8:
    return 0
  return d + 1

# 물고기 이동
def move_fish(graph):
  # 남은 물고기 번호들 찾기
  left_fishes = []
  for i in range(4):
    for j in range(4):
      if graph[i][j] != -1 and graph[i][j] != 0:
        left_fishes.append(graph[i][j][0])
  # 제일 작은 번호부터 이동
  left_fishes.sort()
  for fish_num in left_fishes:
    fish_x, fish_y = -1, -1
    # 번호에 맞는 물고기 찾기
    for i in range(4):
      for j in range(4):
        if graph[i][j] != -1 and graph[i][j] != 0:
          if graph[i][j][0] == fish_num:
            fish_x, fish_y = i, j
    # 물고기 이동
    nx = fish_x + dx[(graph[fish_x][fish_y][1]) - 1]
    ny = fish_y + dy[(graph[fish_x][fish_y][1]) - 1]
    # 갈 수 있다면 (상어 x 경계 이탈 x)
    if 0 <= nx and nx < 4 and 0 <= ny and ny < 4 and graph[nx][ny] != -1:
      temp = graph[nx][ny]
      graph[nx][ny] = graph[fish_x][fish_y]
      graph[fish_x][fish_y] = temp
    # 만약 갈 수 없다면 rotate (상어가 있거나 경계를 벗어날 경우)
    else:
      rotate_d = graph[fish_x][fish_y][1]
      while True:
        rotate_d = rotate(rotate_d)
        rotate_nx = fish_x + dx[rotate_d - 1]
        rotate_ny = fish_y + dy[rotate_d - 1]
        if 0 <= rotate_nx and rotate_nx < 4 and 0 <= rotate_ny and rotate_ny < 4 and graph[rotate_nx][rotate_ny] != -1:
          temp = graph[rotate_nx][rotate_ny]
          graph[rotate_nx][rotate_ny] = graph[fish_x][fish_y]
          graph[fish_x][fish_y] = temp
          break;       

def DFS(graph, result, now_x, now_y, now_d):
  temp_graph = move_fish(graph)
  # 상어 이동 경우의 수 도출
  cases = []
  while True:
    nx = now_x + dx[now_d]
    ny = now_d + dy[now_d]
    if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
      cases.append((nx, ny))
    else:
      break
  max = -1
  # 상어 이동
  for case in cases:
    case_d = graph[case[0]][case[1]][1]
    temp_v = temp_graph[case[0]][case[1]]
    temp_graph[case[0]][case[1]] = 0
    result += graph[case[0]][case[1]][0]
    max = max(DFS(temp_graph, result, case[0], case[1], case_d), max)
    result -= graph[case[0]][case[1]][0]
    temp_graph[case[0]][case[1]] = temp_v    
  return result

result = DFS(graph, result, now_x, now_y, now_d)
print(result)

#########################################