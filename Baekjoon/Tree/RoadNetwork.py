# [도로 네트워크]
# 3176번
import sys
from math import log2
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

LOG = int(log2(n)) + 1
parent = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)
level = [0] * (n+1)
dp = [[[0, 0, 0] for _ in range(LOG)] for _ in range(n+1)]

def DFS(now, depth):
  visited[now] = True
  level[now] = depth
  for next, cost in graph[now]:
    if not visited[next]:
      dp[next][0] = [now, cost, cost]
      DFS(next, depth + 1)
      
DFS(1, 0)
for j in range(1, LOG):
  for i in range(1, n+1):
    dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
    dp[i][j][1] = min(dp[i][j-1][1], dp[dp[i][j-1][0]][j-1][1])
    dp[i][j][2] = max(dp[i][j-1][2], dp[dp[i][j-1][0]][j-1][2])

def LCA(a, b):
  if level[a] > level[b]:
    a, b = b, a
  min_value = INF
  max_value = 0
  for i in range(LOG, -1, -1):
    if level[b] - level[a] >= (1 << i):
      min_value = min(min_value, dp[a][i][1])
      max_value = max(max_value, dp[a][i][2])
      b = dp[b][i][0]
      
  if a == b:
    return min_value, max_value
    
  for i in range(LOG-1, -1, -1):
    if dp[a][i][0] != dp[b][i][0]:
      min_value = min(min_value, dp[a][i][1], dp[b][i][1])
      max_value = min(max_value, dp[a][i][2], dp[b][i][2])
      a = dp[a][i][0]
      b = dp[b][i][0]
  min_value = min(min_value, dp[a][0][1], dp[b][0][1])
  max_value = max(max_value, dp[a][0][2], dp[b][0][2])
  return min_value, max_value
  
INF = float('inf')
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
  a, b = map(int, sys.stdin.readline().split())
  print(*LCA(a, b))
# LCA를 하면서 부모를 찾음
# 부모를 찾는 과정에서 가장 짧은 도로 and 긴 도로를 구해야함
