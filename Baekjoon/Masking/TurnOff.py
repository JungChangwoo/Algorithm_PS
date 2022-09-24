# [불 끄기]
# 14939번
import sys
import copy
graph = []
for _ in range(10):
  data = list(sys.stdin.readline().rstrip())
  for i in range(10):
    if data[i] == '#':
      data[i] = 0
    else:
      data[i] = 1
  graph.append(data)
# 가운데, 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

result = []

def press(graph, x, y):
  for d in range(5):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < 10 and 0 <= ny < 10:
      graph[nx][ny] = not graph[nx][ny]

for case in range(1 << 10):
  temp_graph = copy.deepcopy(graph)
  count = 0

  mask = 1
  for j in range(10):
    if case & mask:
      press(temp_graph, 0, j)
      count += 1
    mask <<= 1
      
  for i in range(1, 10):
    for j in range(10):
      if temp_graph[i-1][j]:
        press(temp_graph, i, j)
        count += 1
  if sum(temp_graph[9]) == 0:
    result.append(count)
    
if len(result) == 0:
  print(-1)
else:
  print(min(result))