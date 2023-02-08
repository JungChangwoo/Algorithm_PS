# [아기 상어]
# 16236번
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = -1, -1
size = 2
eat = 0

for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      sx, sy = i, j
      graph[i][j] = 0
      break

def find_fish(x, y, n, size):
  fishes = []
  visited = [[False] * n for _ in range(n)]
  
  q = deque([(x, y, 0)])
  visited[x][y] = True
  min_count = int(1e9)
  
  while q:
    x, y, count = q.popleft()

    if count > min_count:
      break
    
    if 1 <= graph[x][y] < size:
      fishes.append((x, y, count))
      min_count = count
    
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        if not visited[nx][ny] and graph[nx][ny] <= size:
          visited[nx][ny] = True
          q.append((nx, ny, count + 1))

  if len(fishes) == 0:
    return None
  else:
    fishes.sort(key = lambda x: (x[0], x[1]))
    return fishes[0]

result = 0
while True:
  fish = find_fish(sx, sy, n, size)
  if fish == None:
    break

  tx, ty, count = fish
  sx, sy = tx, ty
  graph[sx][sy] = 0
  result += count
  
  eat += 1
  if eat == size:
    size += 1 
    eat = 0

print(result)



# 1. 먹을 수 있는 물고기 찾기 BFS (새로운 그래프에 표시) 
# 1-1. 만약 없다면 break
# 2. 물고기 정렬
# 2-1. 해당 물고기로 이동 AND 그래프에서 지우기
# 3. 1, 2 반복