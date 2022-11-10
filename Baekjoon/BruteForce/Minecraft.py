# [마인크래프트]
# 18111번
import sys
n, m, b = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

cost = int(1e9)
height = 0
for h in range(257):
  take = 0
  use = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] > h:
        take += graph[i][j] - h
      else:
        use += h - graph[i][j]
        
  if use > take + b:
    continue
  
  value = take * 2 + use
  if cost >= value:
    cost = value
    height = h
print(cost, height)
