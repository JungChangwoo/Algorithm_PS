# [RGB 거리]
# 1149번

import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n):
  for j in range(3):
    # 빨
    if j == 0:
      graph[i][j] = min(graph[i-1][j+1], graph[i-1][j+2]) + graph[i][j]
    if j == 1:
      graph[i][j] = min(graph[i-1][j-1], graph[i-1][j+1]) + graph[i][j]
    if j == 2:
      graph[i][j] = min(graph[i-1][j-2], graph[i-1][j-1]) + graph[i][j]

print(min(graph[n-1]))