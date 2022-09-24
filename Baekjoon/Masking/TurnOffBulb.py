# [전구 끄기]
# 14927번
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def press(graph, x, y):
  for d in range(5):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
      graph[nx][ny] = not graph[nx][ny]

result = []
for case in range(1 << n):
  temp_graph = []
  for i in range(n):
    temp_graph.append(graph[i][:])
  count = 0

  mask = 1
  for j in range(n):
    if case & mask:
      press(temp_graph, 0, j)
      count += 1
    mask <<= 1

  for i in range(1, n):
    for j in range(n):
      if temp_graph[i-1][j]:
        press(temp_graph, i, j)
        count += 1

  if sum(temp_graph[n-1]) == 0:
    result.append(count)

if len(result) == 0:
  print(-1)
else:
  print(min(result))
  