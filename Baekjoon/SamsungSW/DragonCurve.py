# [드래곤 커브]
# 15685번
import sys
graph = [[False] * 101 for _ in range(101)]
n = int(sys.stdin.readline().rstrip())
curves = []
for _ in range(n):
  curves.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 우, 상, 좌, 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def turn(d):
  d += 1
  if d == 4:
    return 0
  return d

from collections import deque
import copy
# 이동방향 정보를 return
def simulate(d, g):
  count = 0
  q = deque()
  q.append(d)
  if g == 0:
    return q
  while True:
    new_q = copy.deepcopy(q)
    while q:
      new_d = turn(q.pop())
      new_q.append(new_d)
    q = copy.deepcopy(new_q)
    count += 1
    if count == g:
      return new_q

def move(x, y, moves):
  while moves:
    d = moves.popleft()
    x += dx[d]
    y += dy[d]
    graph[x][y] = True

# Q에서 q -> new 복제 while q: pop -> turn -> new.append
for curve in curves:
  y, x, d, g = curve
  moves = simulate(d, g)
  graph[x][y] = True
  move(x, y, moves)

result = 0
for i in range(100):
  for j in range(100):
    if graph[i][j] and graph[i][j+1] and graph[i+1][j] and graph[i+1][j+1]:
      result += 1
print(result)