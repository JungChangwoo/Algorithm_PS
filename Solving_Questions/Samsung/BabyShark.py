# [아기 상어]
# 난이도: 중상
# 권장 풀이 시간: 50분
# 시간 제한: 2초
# 메모리 제한: 512MB

n = int(input())
graph = []

for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  
# 상화좌우 벡터
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

shark = (0, 0)
sharkSize = 2

# 처음 상어 위치 찾기
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      shark = (i, j)
      graph[i][j] = 0

# 먹이 찾기
from collections import deque
def find_fish(graph, start, visited):
  q = deque([start])
  visited[start[0]][start[1]] = True
  while q:
    x, y = q.popleft()
    result = []
    # 상하좌우 이동
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
      if graph[nx][ny] > sharkSize:
        continue
      if visited[nx][ny]:
        continue
      if 1 <= graph[nx][ny] < sharkSize:
        result.append((nx, ny))
      x = nx
      y = ny
      visited[x][y] = True
      q.append((x, y))
    # 물고기 확인
    if len(result) == 1:
      return result[0]
    elif len(result) >=2:
      result.sort()
      return result[0]
  return (-1, -1)
  
count = 0
eat = 0
while True:
  visited = [[False for _ in range(n)] for _ in range(n)]
  x, y = find_fish(graph, shark, visited)
  if x == -1:
    break
  count += abs((shark[0] - x)) + abs((shark[1] - y))
  eat += 1
  if sharkSize == eat:
    sharkSize += 1
    eat = 0
  graph[x][y] = 0
  shark = (x, y)

print(count)
# 이동
# BFS로 먹을 수 있는 물고기를 찾음(이때, 이동가능유무를 확인하면서)
# 더이상 먹을 수 있는 물고기가 없다면 끝
# 만약 1개라면 바로 이동
# 여러 개라면 가장 위의 왼쪽 (i가 작고 j가 작은 것)
# 섭취 (크기 증가 유무 확인)


# [이동 유무 및 섭취]
# > 지나갈 수 없음
# = 지나갈 수 있음
# < 먹을 수 있으며 지나갈 수 있음

# [이동 방식]
# 더이상 먹을 수 있는 물고기가 없다면 끝
# 물고기가 1마리 = 물고기 먹으러 
# 물고기가 여러 마리 가장 가까운 물고기 (물고기 중 가장 위 -> 가장 왼) BFS

# [물고기 섭취]
# 먹은 흔적 X
# 크기만큼의 물고기 수를 섭취하면 크기 1증가
# 처음 상어 크기 2


