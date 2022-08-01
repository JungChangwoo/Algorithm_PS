# [바이러스]
# 2606

import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

result = 0
from collections import deque
def BFS(graph, start, visited):
  global result
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    for i in graph[now]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        result += 1

BFS(graph, 1, visited)
print(result)
