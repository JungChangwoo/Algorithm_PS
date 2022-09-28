# [정점들의 거리]
# 1761번
import sys
import math
from collections import deque

n = int(sys.stdin.readline().rstrip())
LOG = int(math.log2(n)) + 1
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

q = deque([(1, 1)])
level = [0] * (n+1)
level[1] = 1
dp = [[[0, 0] for _ in range(LOG)] for _ in range(n+1)]

while q:
  now, cost = q.popleft()
  for next, dist in graph[now]:
    if not level[next]:
      level[next] = cost + 1
      dp[next][0] = [now, dist]
      q.append((next, cost + 1))

for j in range(1, LOG):
  for i in range(1, n+1):
    dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
    dp[i][j][1] = dp[dp[i][j-1][0]][j-1][1] + dp[i][j-1][1]
    
def LCA(a, b):
  total = 0
  if level[a] > level[b]:
    a, b = b, a
  for i in range(LOG-1, -1, -1):
    if level[b] - level[a] >= (1 << i):
      total += dp[b][i][1]
      b = dp[b][i][0]
  if a == b:
    return total
  for i in range(LOG-1, -1, -1):
    if dp[a][i][0] != dp[b][i][0]:
      total += dp[a][i][1]
      total += dp[b][i][1]
      a = dp[a][i][0]
      b = dp[b][i][0]
  total += dp[a][0][1]
  total += dp[b][0][1]
  return total

for _ in range(int(sys.stdin.readline().rstrip())):
  a, b = map(int, sys.stdin.readline().split())
  print(LCA(a, b))