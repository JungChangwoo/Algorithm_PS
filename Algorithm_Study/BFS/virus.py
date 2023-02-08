# [바이러스]
# 2606번
import sys
from collections import deque

def bfs(start):
  count = 0
  q = deque([(start)])
  visited[start] = True
  while q:
    now = q.popleft()
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        q.append(next)
        count += 1
  return count

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(int(sys.stdin.readline().rstrip())):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

print(bfs(1))

  