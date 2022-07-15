# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

###################################################################
# DFS 메서드 정의
def DFS(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)

DFS(graph, 1, visited)
###################################################################
from collections import deque
visited2 = [False] * 9 # DFS에서 쓴 거 초기화
# BFS 메서드 정의
def BFS(graph, start, visited):
  queue = deque([start]) # 리스트를 생성자에 넣을 수 있음
  visited2[start] = True
  # 큐가 빌 때까지 반복
  while queue: 
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited2[i]:
        visited2[i] = True
        queue.append(i)

BFS(graph, 1, visited2)
    