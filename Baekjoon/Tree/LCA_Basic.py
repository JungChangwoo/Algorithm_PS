# [가장 가까운 공통 조상]
# 3584번
import sys
import math
from collections import deque

def BFS(start):
  q = deque([(start, 1)])
  level[start] = 1
  while q:
    now, dist = q.popleft()
    for next in graph[now]:
      if not level[next]:
        level[next] = dist + 1
        dp[next][0] = now
        q.append((next, dist + 1))

def LCA(a, b):
  if level[a] > level[b]:
    a, b = b, a
  for i in range(LOG-1, -1, -1):
    if level[b] - level[a] >= (1 << i):
      b = dp[b][i]
  if a == b:
    return a
  for i in range(LOG-1, -1, -1):
    if dp[a][i] != dp[b][i]:
      a = dp[a][i]
      b = dp[b][i]
  return dp[a][0]
  
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  n = int(sys.stdin.readline().rstrip())
  LOG = int(math.log2(n)) + 1
  graph = [[] for _ in range(n+1)]
  start = 0
  for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    if i == 0:
      start = a

  level = [0] * (n+1)
  dp = [[0 for _ in range(LOG)] for _ in range(n+1)]
  BFS(start)
  
  for j in range(1, LOG):
    for i in range(1, n+1):
      dp[i][j] = dp[dp[i][j-1]][j-1]
  
  A, B = map(int, sys.stdin.readline().split())
  print(LCA(A, B))
