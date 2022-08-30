# 줄 세우기
# 2252번
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
in_count = [0] * (n+1)
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  in_count[b] += 1

def OrderLine():
  q = deque()
  for i in range(1, n+1):
    if in_count[i] == 0:
      q.append(i)
  while q:
    now = q.popleft()
    print(now, end=' ')
    for next in graph[now]:
      in_count[next] -= 1
      if in_count[next] == 0:
        q.append(next)

OrderLine()
