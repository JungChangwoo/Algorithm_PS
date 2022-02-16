# [연구소]
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다. 이때, 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳입니다. 아무런 벽을 세우지 않으면 바이러스는 모든 빈칸으로 퍼져나갈 수 있습니다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 합니다. 당신은 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
# (3 <= n, m <= 8)

# 나의 답
n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

wallCombination = []
birus = []

# 방향 벡터
arrayX = [-1, 1, 0, 0] # 상 하 좌 우
arrayY = [0, 0, -1, 1] # 상 하 좌 우
# 방문
visited = [[False for i in range(m)] for i in range(n)]

# 벽이 세워질 수 있는 모든 인덱스 and 바이러스가 있는 모든 인덱스 구함
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      wallCombination.append((i, j))
    if graph[i][j] == 2:
      birus.append((i, j))

# 벽이 세워질 수 있는 모든 조합을 구함
from itertools import combinations
wallCombination = list(combinations(wallCombination, 3))

# 가상 그래프
import copy
graphCopy = copy.deepcopy(graph)


from collections import deque
# 바이러스 퍼트리기 메소드
def spreadBirus(graphCopy, birus, visited):
  result = 0
  # 바이러스 하나씩 퍼트리기
  for bi in birus:
    q = deque([bi])
    visited[bi[0]][bi[1]] = True
    while q:
      v = q.popleft() # (0,1)
      # 상하좌우
      for i in range(4):
        vi = v[0] + arrayX[i]
        vj = v[1] + arrayY[i]
        # 갈 수 없는 길일 때
        if vi < 0 or vi >= n or vj < 0 or vj >= m:
          continue
        # 벽일 때 or 이미 퍼진 파이러스라면
        if graph[vi][vj] == 1:
          continue
        # 갈 수 있다면
        if not visited[vi][vj]:
          visited[vi][vj] = True
          graphCopy[vi][vj] == 2
          q.append((vi, vj))
  # 안전 영역 계산
  for i in range(n):
    for j in range(m):
      if graphCopy[i][j] == 0:
        result += 1
  return result

result = 0

# 벽이 세워질 수 있는 조합 케이스를 하나씩 확인
for wallCase in wallCombination:
  # 가상 그래프에 벽 세우기
  for wall in wallCase:
    i, j = wall[0], wall[1]
    graphCopy[i][j] = 1
  # 바이러스 퍼뜨리고 안전영역 계산
  result = max(result, spreadBirus(graphCopy, birus, visited))
  print(graphCopy)
  # 가상 그래프 초기화
  graphCopy = copy.deepcopy(graph)

print(result)

##############################################################3
# 이코테 답
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 상, 하 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 바이러스 배치하고 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# DFS를 이용해 울타리를 설치하면서 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
###############################################################
# - 하나의 함수에서 여러 개를 하려고 하지 말고 분할
# - 울타리 설치할 때를 DFS로,,, 
# => 부분 구조의 반복으로 답을 도출해낼 수 있는지
# => 탈출 조건을 어떻게 설정할 것이며, 초기화는 어떻게 할 것인지