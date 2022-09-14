# [열쇠]
# 9328번

# 찾은 열쇠 유무
# 1. BFS를 돌면서 열쇠를 찾는다.
# 2. 끝까지 돈 후 찾은 열쇠가 열 수 있는 모든 문을 연다.
# 3. 더이상 찾을 수 있는 열쇠가 없으면 그만두고 마지막으로 BFS를 하며 문서를 찾는다.
from collections import deque
def BFS(get_keys):
  visited = [[False] * (w+2) for _ in range(h+2)]
  q = deque()
  q.append((0, 0))
  visited[0][0]
  result = 0

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < h+2 and 0 <= ny < w+2:
        if visited[nx][ny] == False and (graph[nx][ny] != '*' and graph[nx][ny].isupper() == False):
          q.append((nx, ny))
          visited[nx][ny] = True
          # 만약, 열쇠라면 담는다.
          if graph[nx][ny].islower():
            get_keys.append(graph[nx][ny])
            graph[nx][ny] = '.'
          # 만약, 문서라면 결과값 증가
          elif graph[nx][ny] == '$':
            result += 1
  return result
  
def open(key):
  key = key.upper()
  for i in range(1, h+1):
    for j in range(1, w+1):
      if graph[i][j] == key:
        graph[i][j] = '.'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  h, w = map(int , sys.stdin.readline().split())
  graph = []
  graph.append(['.'] * (w+2))
  for _ in range(h):
    graph.append(['.'] + list(sys.stdin.readline().rstrip()) + ['.'])
  graph.append(['.'] * (w+2))

  keys_string = sys.stdin.readline().rstrip()
  keys = []
  if keys_string != '0':
    keys = list(keys_string)

  # 가지고 있는 열쇠로 열 수 있는 모든 문을 연다.
  for key in keys:
    open(key)
  while True:
    get_keys = []
    result = BFS(get_keys)
    # 얻은 열쇠로 열 수 있는 모든 문을 연다.
    for key in get_keys:
      if key in keys:
        continue
      keys.append(key)
      open(key)
    # 만약, 더이상 얻을 수 있는 열쇠가 없다면 문서를 구하고 return
    if len(get_keys) == 0:
      print(result)
      break