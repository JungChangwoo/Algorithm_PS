# [ACM Craft]
# 1005번

import sys
from collections import deque
def topological_sort():
  # 들어오는 간선이 없는 것을 담음
  q = deque()
  for i in range(1, len(in_count)):
    if in_count[i] == 0:
      q.append((data[i-1], i))
      distance[i] = data[i-1]
  while q:
    dist, now = q.popleft()
    for next in graph[now]:
      in_count[next] -= 1
      distance[next] = max(distance[next], distance[now] + data[next-1])
      if in_count[next] == 0:
        q.append((distance[next], next))
  
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  n, k = map(int, sys.stdin.readline().split())
  data = list(map(int, sys.stdin.readline().split()))
  distance = [-1] * (n+1)
  in_count = [0] * (n+1)
  graph = [[] for _ in range(n+1)]
  for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    in_count[b] += 1
  w = int(sys.stdin.readline().rstrip())
  topological_sort()
  print(distance[w])