# [경쟁적 전염]
# N x N 크기의 시험관이 있습니다. 특정한 위치에는 바이러스가 존재할 수 있으며 바이러스의 종류는 1~K번까지 있습니다. 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식하는데, 매초 번호가 낮은 바이러스부터 먼저 증식합니다. S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력하시오. 만약, 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력합니다.

n, k = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1] # 상, 하, 좌, 우

from collections import deque
def BFS(graph, s, k):
  queue = deque()
  # 바이러스 찾기
  viruses = []
  for i in range(n):
    for j in range(n):
      if graph[i][j] != 0:
        virus = graph[i][j]
        x, y = i, j
        viruses.append((virus, x, y))
  viruses.sort()
  for virus in viruses:
    queue.append(virus)
    graph[virus[1]][virus[2]] = virus[0]
  # s만큼 반복하기 위해
  now = (0, 0, 0)
  prev = (0, 0, 0)
  count = -1
  # 큐가 빌 때까지
  while queue:
    now = queue.popleft()
    if prev[0] == 3 and now[0] == 1:
      count += 1
      if count == s:
        break
    v, x, y = now[0], now[1], now[2]
    graph[x][y] = v
    # 상, 하, 좌, 우
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if tx < 0 or tx >= n or ty < 0 or ty >= n:
        continue
      if graph[tx][ty] != 0:
        continue
      queue.append((v, tx, ty))
      graph[tx][ty] = 9999
    prev = now

BFS(graph, s, k)

result = 0
if graph[x-1][y-1] == 9999:
  result = 0
else:
  result = graph[x-1][y-1]
print(result)

########################################################################
# 이코테 답
n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])

# [배운 점]
# BFS가 한 사이클을 돌 때마다 그 단계를 어떻게 기록할 수 있을까?
# => 사이클을 계산하는 속성을 하나 추가해서 append를 할 때 기록하면 된다.




