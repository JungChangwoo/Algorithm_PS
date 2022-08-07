# [연구소]
# 14502
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 빈 칸의 위치 and 바이러스 위치를 모두 구한다.
cases = []
viruss = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      cases.append((i, j))
    if graph[i][j] == 2:
      viruss.append((i, j))
# 3 개의 벽을 세울 수 있는 모든 경우의 수
from itertools import combinations
cases = list(combinations(cases, 3))

# 바이러스 퍼뜨리기
from collections import deque
def BFS(graph, start, visited):
  q = deque([start])
  visited[start[0]][start[1]] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
          if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            visited[nx][ny] = True
            q.append((nx, ny))
  return graph

# 경우의 수를 하나씩 확인
import copy
def Laboratory(graph):
  global result
  for case in cases:
    new_graph = copy.deepcopy(graph)
    # 벽 세우기
    for i in case:
      new_graph[i[0]][i[1]] = 1
    # 바이러스 퍼뜨림 (BFS)
    visited = [[False] * m for _ in range(n)]
    for virus in viruss:
      new_graph = BFS(new_graph, virus, visited)
    # 안전영역 구하기
    total = 0
    for i in range(n):
      for j in range(m):
        if new_graph[i][j] == 0:
          total += 1
    result = max(result, total)

Laboratory(graph)
print(result)