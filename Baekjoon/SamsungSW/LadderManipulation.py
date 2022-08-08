# [사다리 조작]
# 15684번
import sys
n, m, h = map(int, sys.stdin.readline().rstrip().split())
graph = [[False] * n for _ in range(h)]
ladders = []
for i in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a-1][b-1] = True
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def go(i):
  x, y = -1, i
  while True:
    # 아래로 이동
    nx = x + dx[1]
    ny = y + dy[1]
    # 만약 도착했다면
    if nx == h:
      if i == ny:
        return True
      else:
        return False
    # 만약 가로선이 있다면 왼쪽 or 오른쪽 이동
    x, y = nx, ny
    if graph[nx][ny]:
      x += dx[3]
      y += dy[3]
    elif graph[nx][ny - 1]:
      x += dx[2]
      y += dy[2]
      
def simulate():
  # i ~ n번 실행  
  for i in range(n):
    if go(i) == False:
      return False
  return True

def DFS(count, num, xidx, yidx):
  global result
  # num 갯수 만큼의 가로선을 추가했다면
  if count == num:
    if simulate():
      result = min(result, count)
    return
  # 가로선을 놓을 수 있는 경우의 수를 구한다.
  for i in range(xidx, h):
    for j in range(n):
      if i == xidx and count != 0:
        j = yidx + 2
      if j + 1 < n:
        if graph[i][j] == False and graph[i][j+1] == False:
          graph[i][j] = True
          DFS(count + 1, num, i, j)
          graph[i][j] = False

result = int(1e9)
for i in range(4):
  DFS(0, i, 0, 0)
# 3보다 크거나 불가능하다면
if result == int(1e9):
  print(-1)
else:
  print(result)
