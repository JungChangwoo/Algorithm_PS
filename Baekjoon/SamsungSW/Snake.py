# [뱀]
import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
graph = [[0] * n for _ in range(n)]
graph[0][0] = 2
for i in range(k):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x-1][y-1] = 1
l = int(sys.stdin.readline().rstrip())
moveInfo = []
for i in range(l):
  data = input().split()
  moveInfo.append(data)

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_right(d):
  d += 1
  if d == 4:
    return 0
  return d

def turn_left(d):
  d -= 1
  if d == -1:
    return 3
  return d

def getDirection(count, d):
  for i in moveInfo:
    if int(i[0]) == count:
      if i[1] == 'D':
        d = turn_right(d) 
      else:
        d = turn_left(d)
  return d 

def move(graph, snake, d):
  x, y = snake
  nx = x + dx[d]
  ny = y + dy[d]
  if nx < 0 or nx >= n or ny < 0 or ny >= n:
    return False
  if graph[nx][ny] == 2:
    return False
  if graph[nx][ny] == 1:
    graph[nx][ny] = 2
    path.append((nx, ny))
  else:
    graph[nx][ny] = 2
    path.append((nx, ny))
    tailX, tailY = path.popleft()
    graph[tailX][tailY] = 0
  snake = (nx, ny)
  return graph, snake
  
d = 1
count = 1
snake = (0, 0)
from collections import deque
path = deque()
path.append((0, 0))
while True:
  # 방향 정보 확인
  d = getDirection(count-1, d)
  moveResult = move(graph, snake, d)
  # 이동
  if moveResult == False:
    break
  else:
    graph, snake = moveResult
  count += 1

print(count)


# 이동
# 자기몸 or 벽 => 끝
# 만약, 사과를 먹었다면 몸 길이 안 줄어듬
