# [2048[Easy]]
# 10240
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import copy
def move(graph, d):
  graph = copy.deepcopy(graph)
  union = []
  # 상
  if d == 0:
    for i in range(1, n):
      for j in range(n):
        x, y = i, j
        while True:
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 > nx or nx >= n or 0 > ny or ny >= n:
            break
          # 숫자와 만났다면
          if graph[nx][ny] != 0:
            # 숫자가 같으며 이전에 합쳐진 적이 없는 칸이라면
            if graph[x][y] == graph[nx][ny] and (nx, ny) not in union:
              graph[nx][ny] = graph[x][y] + graph[nx][ny]
              graph[x][y] = 0
              union.append((nx, ny))
            break
          # 숫자와 만나지 않았다면 계속 이동
          else:
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            x, y = nx, ny
  # 하
  if d == 1:
    for i in range(n-1, -1, -1):
      for j in range(n):
        x, y = i, j
        while True:
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 > nx or nx >= n or 0 > ny or ny >= n:
            break
          if graph[nx][ny] != 0:
            if graph[x][y] == graph[nx][ny] and (nx, ny) not in union:
              graph[nx][ny] = graph[x][y] + graph[nx][ny]
              graph[x][y] = 0
              union.append((nx, ny))
            break
          else:
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            x, y = nx, ny
  # 좌
  if d == 2:
    for i in range(n):
      for j in range(1, n):
        x, y = i, j
        while True:
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 > nx or nx >= n or 0 > ny or ny >= n:
            break
          if graph[nx][ny] != 0:
            if graph[x][y] == graph[nx][ny] and (nx, ny) not in union:
              graph[nx][ny] = graph[x][y] + graph[nx][ny]
              graph[x][y] = 0
              union.append((nx, ny))
            break
          else:
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            x, y = nx, ny
  # 우
  if d == 3:
    for i in range(n):
      for j in range(n-1, -1, -1):
        x, y = i, j
        while True:
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 > nx or nx >= n or 0 > ny or ny >= n:
            break
          if graph[nx][ny] != 0:
            if graph[x][y] == graph[nx][ny] and (nx, ny) not in union:
              graph[nx][ny] = graph[x][y] + graph[nx][ny]
              graph[x][y] = 0
              union.append((nx, ny))
            break
          else:
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            x, y = nx, ny
  return graph

def getMax(graph):
  value = 0
  for i in range(n):
    value = max(value, max(graph[i]))
  return value
  
result = 0
def BFS(graph, count):
  global result
  q = deque()
  q.append((graph, count))
  while q:
    graph, count = q.popleft();
    # 최대 이동횟수 넘어가면 return
    if count == 6:
      return
    for i in range(4):
      moveGraph = move(graph, i)
      q.append((moveGraph, count + 1))
      if count == 5:
        moveResult = getMax(moveGraph)
        result = max(result, moveResult)

BFS(graph, 1)
print(result)