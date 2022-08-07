# [로봇 청소기]
# 14503번
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
robot = list(map(int, sys.stdin.readline().rstrip().split()))
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]
def turn_left(d):
  d -= 1
  if d == -1:
    return 3
  return d

def back(d):
  d = turn_left(d)
  d = turn_left(d)
  return d

result = 0
while True:
  # 청소
  x, y, d = robot
  visited[x][y] = True
  result += 1
  # 탐색 and 이동
  isOkay = False
  for i in range(4):
    d = turn_left(d)
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
      if not visited[nx][ny]:
        if graph[nx][ny] == 0:
          robot = [nx, ny, d]
          isOkay = True
          break
  # 바라보는 방향을 유지한 채로 한 칸 후진
  if isOkay == False:
    back_d = back(d)
    nx = x + dx[back_d]
    ny = y + dy[back_d]
    robot = [nx, ny , d]
    result -= 1
    # 만약, 뒤쪽 방향도 벽인 경우
    if 0 > nx or nx >= n or 0 > ny  or ny >= m:
      result += 1
      print(result)
      break
    if graph[nx][ny] == 1:
      result += 1
      print(result)
      break

        
# 청소 (visited)
# turn_left
# 청소하지 않았다면 이동 and 청소 (not visited => visited)
# 4방향 모두 청소 했거나 벽인 경우는 후퇴 (뒤로 가기)
# 후진도 할 수 없는 경우에 stop (뒤 == 1 => return)

