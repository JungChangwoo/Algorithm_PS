import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [[0] * n for _ in range(n)]
for _ in range(int(sys.stdin.readline().rstrip())):
  x, y = list(map(int, sys.stdin.readline().split()))
  graph[x-1][y-1] = 1

opers = dict()
for _ in range(int(sys.stdin.readline().rstrip())):
  second, oper = sys.stdin.readline().split()
  opers[int(second)] = oper

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left(d):
  d -= 1
  if d == -1:
    return 3
  return d
def turn_right(d):
  d += 1
  if d == 4:
    return 0
  return d

def get_d(second, d):
  if opers.get(second) != None:
    if opers[second] == 'L':
      return turn_left(d)
    else:
      return turn_right(d)
  return d

snake = deque()
snake.append((0, 0))
graph[0][0] = 2
d = 1
second = 0

while True:
  second += 1
  x, y = snake[-1]
  nx = x + dx[d]
  ny = y + dy[d]
  if nx < 0 or nx >= n or ny < 0 or ny >= n:
    print(second)
    break
  if graph[nx][ny] == 2:
    print(second)
    break
  if graph[nx][ny] == 0:
    tx, ty = snake.popleft()
    graph[tx][ty] = 0
  graph[nx][ny] = 2
  snake.append((nx, ny))

  d = get_d(second, d)


  

# if 사과 = 몸길이 안 줄임
# else = 몸길이 줄임
# if 시간 확인 후 방향 전환