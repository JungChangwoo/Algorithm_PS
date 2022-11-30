# [화성 탐사]
# 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 합니다. 화성 탐사 기계가 존재하는 공간은 N x N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용이 존재합니다. 가장 왼쪽 위 칸인 위치에서 가장 오른쪽 아래 칸인 위치로 이동하는 최소비용을 출력하는 프로그램을 작성하세요. 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있습니다.


# 나의 답
dx = [1, -1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

import heapq
def find(n, startX, startY):
  q = []
  heapq.heappush(q, (graph[startX][startY],startX, startY))
  distance[startX][startY] = graph[startX][startY]
  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    # 인접 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))

t = int(input())
for _ in range(t):
  n = int(input())
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))
  INF = 9999
  distance = [[INF for _ in range(n)] for _ in range(n)]
  
  find(n, 0, 0)
  result = distance[n-1][n-1]
  print(result)
  