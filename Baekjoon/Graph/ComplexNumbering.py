# [단지번호붙이기]
# 2667

import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
  data = list(map(int, sys.stdin.readline().rstrip()))
  graph.append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS(graph, start, number):
  count = 0
  q = deque([start])
  while q:
    x, y = q.popleft()
    graph[x][y] = number
    count += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if graph[nx][ny] == 1:
          q.append((nx, ny))
          graph[nx][ny] = number
  return count
  
number = 2
result = []
# 모든 지점을 확인해본다.
for i in range(n):
  for j in range(n):
    # 만약, 아직 방문하지 않은 곳이라면 BFS
    if graph[i][j] == 1:
      count = BFS(graph, (i, j), number)
      result.append(count)
      number += 1

print(len(result))
result.sort()
for i in result:
  print(i)