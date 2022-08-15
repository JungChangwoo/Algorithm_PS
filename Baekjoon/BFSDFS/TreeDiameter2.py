# [트리의 지름]
# 1967번

import sys
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b, cost = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append((b, cost))
  graph[b].append((a, cost))

from collections import deque
def BFS(start):
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    for i in graph[now]:
      next, cost = i
      if not visited[next]:
        q.append(next)
        visited[next] = True
        distance[next] = distance[now] + cost

visited = [False] * (n+1)
distance = [0] * (n+1)
BFS(1)
start = distance.index(max(distance))

visited = [False] * (n+1)
distance = [0] * (n+1)
BFS(start)
print(max(distance))