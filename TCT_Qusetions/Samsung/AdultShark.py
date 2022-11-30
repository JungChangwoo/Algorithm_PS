# [어른 상어]
# 난이도: 상
# 권장 풀이 시간: 50분
# 시간 제한: 1초

n, m, k = map(int, input().split())
graph = [[[0, 0]] * n for _ in range(n)]
sharks = [[-1, -1, -1] for _ in range(m + 1)]

# 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(len(data)):
    if data[j] != 0:
      graph[i][j] = [data[j], k]
      sharks[data[j]][0] = i
      sharks[data[j]][1] = j

first_direction = list(map(int, input().split()))
for i in range(len(first_direction)):
  sharks[i+1][2] = first_direction[i] - 1

sharks_move = [[] for _ in range(m+1)]
for i in range(m):
  for j in range(4):
    data = list(map(int, input().split()))
    sharks_move[i].append(data)

def get_position(index):
  positions = []
  # 위, 아래, 왼쪽, 오른쪽 확인해서 냄새가 없는 곳 확인
  x, y, d = sharks[index]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if not graph[nx][ny][0] > 0:
        direction = i
        positions.append((nx, ny, direction))
  # 만약, 아무 냄새 없는 칸이 없다면 자신의 냄새로 돌아감
  if len(positions) == 0:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if graph[nx][ny][0] == index:
          direction = i
          positions.append((nx, ny, direction))
  # 만약, 가능한 곳이 한 개라면 해당 해당 포지션을 바로 반환
  if len(positions) == 1:
    return positions[0]
  # 우선순위에 따라 방향 결정
  else:
    # 지금 방향이 무엇인지
    now_direction = sharks[index][2]
    # 해당 방향의 우선순위대로 반복하면서 가능한 포지션 유무 확인
    moves = sharks_move[index-1][now_direction]
    for move in moves:
      for position in positions:
        direction = position[2]
        if (move - 1) == direction:
          return position

def get_remain_shark():
  result = 0
  for shark in sharks:
    if shark[0] != -1:
      result += 1
  return result
    
result = 0
while True:
  result += 1
  # 상어를 뒤에서부터 차례대로 이동
  for i in range(len(sharks)-1, 0, -1):
    # 이동할 포지션 획득
    position = get_position(i)
    next_x, next_y = position[0], position[1]
    direction = position[2]
    # 이동
    sharks[i] = [next_x, next_y, direction]
  # 겹치는 상어 확인
  for i in range(1, len(sharks)):
    for j in range(1, len(sharks)):
      if i == j:
        continue
      if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1]:
        if i < j:
          sharks[j] = [-1, -1, -1]
  # 냄새 뿌리기
  for i in range(1, len(sharks)):
    x, y = sharks[i][0], sharks[i][1]
    graph[x][y] = [i, k + 1]
  # 만약, 1번 상어만 남아있다면 탈출
  remain_shark_num = get_remain_shark()
  if remain_shark_num == 1:
    print(result)
    break
  # 냄새 시간 줄이기
  for i in range(n):
    for j in range(n):
      if graph[i][j][1] > 0:
        graph[i][j][1] -= 1
        if graph[i][j][1] == 0:
          graph[i][j][0] = 0
          
  if result > 1000:
    print(-1)
    break
