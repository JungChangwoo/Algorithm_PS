# [트리의 부모 찾기]
# 11725번

import sys
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)
parent = [i for i in range(n+1)]

from collections import deque
def BFS():
  q = deque([1])
  visited[1] = True
  while q:
    now = q.popleft()
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        q.append(next)
        parent[next] = now
BFS()
for i in range(2, n+1):
  print(parent[i])