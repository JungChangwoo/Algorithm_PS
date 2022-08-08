# [감시]
# 15683번
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

cctvs = []
sgraph = [[False] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if 1 <= graph[i][j] <= 5:
      cctvs.append((i, j, graph[i][j]))
      sgraph[i][j] = True
    if graph[i][j] == 6:
      sgraph[i][j] = True

visited = [False] * len(cctvs)
dx = [-1, 0, 1, 0] # 상, 우, 하, 좌
dy = [0, 1, 0, -1]

def execute(new_sgraph, x, y, d):
  if d == 4:
    d = 0
  if d == -1:
    d = 3
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      return 
    if graph[nx][ny] == 6:
      return 
    else:
      new_sgraph[nx][ny] = True
      x, y = nx, ny

def surveil(new_sgraph, cctv, d):
  x, y, idx = cctv
  # 1번 카메라
  if idx == 1:
    execute(new_sgraph, x, y, d)
  # 2번 카메라
  if idx == 2:
    # 상 or 우 일때만 실행
    if d == 0 or d == 1:
      execute(new_sgraph, x, y, d)  
      execute(new_sgraph, x, y, d + 2) 
  # 3번 카메라
  if idx == 3:
    execute(new_sgraph, x, y, d)
    execute(new_sgraph, x, y, d + 1)
  # 4번 카메라
  if idx == 4:
    execute(new_sgraph, x, y, d)
    execute(new_sgraph, x, y, d + 1)
    execute(new_sgraph, x, y, d - 1)
  # 5번 카메라
  if idx == 5:
    # 상 일때만 실행
    if d == 0:
      execute(new_sgraph, x, y, d)
      execute(new_sgraph, x, y, d + 1)
      execute(new_sgraph, x, y, d + 2)
      execute(new_sgraph, x, y, d + 3)

def next_cctv(count):
  if count >= len(cctvs):
    return False
  else:
    return True

result = int(1e9)
import copy
def DFS(sgraph, count):
  global result
  if len(cctvs) == 0:
    total = 0
    for i in range(n):
      for j in range(m):
        if sgraph[i][j] == False:
          total += 1
    result = total
    return
  cctv = cctvs[count]
  # cctv가 방향을 돌면서 감시
  for d in range(4):
    new_sgraph = copy.deepcopy(sgraph)
    surveil(new_sgraph, cctv, d)
    if next_cctv(count + 1):
      DFS(new_sgraph, count + 1)
    else:
      total = 0
      for i in range(n):
        for j in range(m):
          if new_sgraph[i][j] == False:
            total += 1
      result = min(result, total)
  
DFS(sgraph, 0)
print(result)

