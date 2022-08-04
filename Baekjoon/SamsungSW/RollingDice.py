# [주사위 굴리기]
# 14499
import sys
n, m, x, y, k = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
orders = list(map(int, sys.stdin.readline().rstrip().split()))

dice = [0] * 6
# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(dir):
  global dice
  global graph
  global x, y
  a, b, c, d, e, f = dice
  nx = x + dx[dir-1]
  ny = y + dy[dir-1]
  
  if nx < 0 or nx >= n or ny < 0 or ny >= m:
    return False
  if dir == 1:
    a, b, c, d, e, f = d, b, a, f, e, c
  if dir == 2:
    a, b, c, d, e, f = c, b, f, a, e, d
  if dir == 3:
    a, b, c, d, e, f = e, a, c, d, f, b
  if dir == 4:
    a, b, c, d, e, f = b, f, c, d, a, e

  if graph[nx][ny] == 0:
    graph[nx][ny] = f
  else:
    f = graph[nx][ny]
    graph[nx][ny] = 0
  dice = [a, b, c, d, e, f]   
  x, y = nx, ny
  return True

for order in orders:
  if move(order) == False:
    continue
  else:
    print(dice[0])