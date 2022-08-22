# [N-Queen]
# 9663번

# 1. 퀸을 놓는다.
# 2. 상하좌우대각선 방문한다.
# 3. 다음 칸부터 퀸을 놓을 수 있는 자리 탐색
import copy
# 상, 상우, 우, 우하, 하, 좌하, 좌, 좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def go(visited, x, y, dir):
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      return
    visited[nx][ny] = True
    x, y = nx, ny
    
def visit(visited, x, y):
  # 상하좌우대각선으로 이동
  for i in range(8):
    go(visited, x, y, i)
  
def DFS(visited, x, y, count):
  global result
  visited = copy.deepcopy(visited)
  # 만약, 퀸을 전부 놓았다면 경우의 수 증가
  if count == n:
    result += 1
    return 
  #상하좌우대각선 방문
  visited[x][y] = True
  visit(visited, x, y)
  # 다음 칸부터 자리 탐색
  for i in range(x, n):
    if i==x:
      for j in range(y+1, n):
        if not visited[i][j]:
          visited[i][j] = True
          DFS(visited, i, j, count+1)
          visited[i][j] = False
    else:
      for j in range(0, n):
        if not visited[i][j]:
          visited[i][j] = True
          DFS(visited, i, j, count+1)
          visited[i][j] = False
  
import sys
n = int(sys.stdin.readline().rstrip())
visited = [[False] * n for _ in range(n)]
result = 0
for i in range(n):
  for j in range(n):
    DFS(visited, i, j, 1)
print(result)

###############################################################
import sys
n = int(sys.stdin.readline().rstrip())
visited = [[False] * n for _ in range(n)]
result = 0
row = [0] * n

def promising_check(x):
  # 현재로부터 위의 행들을 살핌
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
  return True
  
def n_queen(x):
  global result
  if x == n:
    result += 1
    return
  # 왼쪽에서 오른쪽으로 퀸을 놓는다. 
  for i in range(n):
    row[x] = i
    if promising_check(x):
      n_queen(x+1)
n_queen(0)
print(result)
# 1. 퀸을 놓는다.
# 2. 공격 범위 방문한다.
# 3. 놓은 다음 칸에 놓을 수 있는 자리를 탐색한다. 