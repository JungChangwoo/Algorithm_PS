# [DFS와 BFS]
# 1260번
import sys
n, m, start = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  graph[b].append(a)
  
visited = [False] * (n+1)

for i in range(1, n+1):
  graph[i].sort()

def DFS(start, visited):
  visited[start] = True
  print(start, end=" ")
  for i in graph[start]:
    if not visited[i]:
      DFS(i, visited)

from collections import deque
def BFS(start, visited):
  q = deque([start])
  visited[start] = True
  while q:
    now = q.popleft()
    print(now, end=" ")
    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

DFS(start, visited)
print()

visited = [False] * (n+1)
BFS(start, visited)