# [트리의 부모 찾기]
# 11725번
import sys
from collections import deque
def bfs(start):
  q = deque([(start)])
  visited[start] = True
  
  while q:
    now = q.popleft()
    for next in graph[now]:
      if not visited[next]:
        parent[next] = now
        visited[next] = True
        q.append(next)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
parent = [i for i in range(n+1)]
visited = [False] * (n+1)

bfs(1)

for i in range(2, n+1):
  print(parent[i])