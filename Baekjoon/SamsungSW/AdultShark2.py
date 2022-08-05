n, m, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
sharkDir = list(map(int, input().split()))
priority = [[] for _ in range(m)]
for i in range(m):
  for j in range(4):
    priority[i].append(list(map(int, input().split())))

smell = [[[0, 0]] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
  for i in range(n):
    for j in range(n):
      if smell[i][j][1] > 0:
        smell[i][j][1] -= 1
      if graph[i][j] != 0:
        smell[i][j] = [graph[i][j], k]

def move_shark():
  new_graph = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      # 상어가 있다면
      if graph[i][j] != 0:
        # 우선순위에 따라서 냄새가 없는 곳이 있는지
        x, y = i, j
        d = sharkDir[graph[i][j] - 1]
        isSmell = False
        for k in range(4):
          nx = x + dx[priority[graph[i][j] - 1][d - 1][k] - 1]
          ny = y + dy[priority[graph[i][j] - 1][d - 1][k] - 1]
          if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 냄새가 없다면
            if smell[nx][ny][1] == 0:
              sharkDir[graph[x][y] - 1] = priority[graph[i][j] - 1][d - 1][k]
              # 상어가 있다면
              if new_graph[nx][ny] != 0:
                new_graph[nx][ny] = min(new_graph[nx][ny], graph[x][y])
              else:
                new_graph[nx][ny] = graph[x][y]
              isSmell = True
              break
        # 만약, 냄새가 없는 곳이 없다면 
        if isSmell == False:
          for k in range(4):
            nx = x + dx[priority[graph[i][j] - 1][d - 1][k] - 1]
            ny = y + dy[priority[graph[i][j] - 1][d - 1][k] - 1]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
              # 자신의 냄새와 같다면
              if smell[nx][ny][0] == graph[i][j]:
                sharkDir[graph[x][y] - 1] = priority[graph[i][j] - 1][d - 1][k]
                new_graph[nx][ny] = graph[x][y]
                graph[x][y] = 0
                break
  return new_graph
time = 0
update_smell()
while True:
  graph = move_shark()
  update_smell()
  time += 1
  isOnlyOne = True
  # 1번 상어만 남아있는지 확인
  for i in range(n):
    for j in range(n):
      if graph[i][j] > 1:
        isOnlyOne = False
  if isOnlyOne:
    print(time)
    break
  if time >= 1000:
    print(-1)
    break
# 상어 움직임 함수
# (우선 순위에 따라서)
# 냄새 뿌리기 함수
# graph (상어 위치만 표시)
# smell (상어 번호와 냄새만 표시)
# sharks, 방향
