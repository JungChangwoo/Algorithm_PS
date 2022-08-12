# [트리의 지름]
# 1167번

import sys
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
  data = list(map(int, sys.stdin.readline().rstrip().split()))
  a = data[0]
  for i in range(1, len(data) - 1, 2):
    b = data[i]
    cost = data[i+1]
    graph[a].append((b, cost))

def DFS(start):
  visited[start] = True
  for i in graph[start]:
    if not visited[i[0]]:
      distance[i[0]] = distance[start] + i[1]
      DFS(i[0])

visited = [False] * (n+1)
distance = [0] * (n+1)
DFS(1)
start = distance.index(max(distance))

visited = [False] * (n+1)
distance = [0] * (n+1)
DFS(start)
print(max(distance))
      
    