# [한동이는 엽업사원!]
# 8012번
import sys
from math import log2
from collections import deque
n = int(sys.stdin.readline().rstrip())
LOG = int(log2(n)) + 1
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

level = [0] * (n+1)
dp = [[[0, 0] for _ in range(LOG)] for _ in range(n+1)]

def BFS():
  q = deque([(1, 1)])
  level[1] = 1
  while q:
    now, cost = q.popleft()
    for next, dist in graph[now]:
      if not level[next]:
        level[next] = cost + 1
        dp[next][0] = [now, dist]
        q.append((next, cost + 1))
BFS()
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
  seung = 0  
  for i in range(LOG-1, -1 -1):
    if dp[a][i][0] != dp[b][i][0]:
      total += dp[a][i][1]
      total += dp[b][i][1]
      a = dp[a][i][0]
      b = dp[b][i][0]
    else:
      print('seung', i)
      seung = i
  
  total += dp[a][seung][1]
  total += dp[b][seung][1]
  return total

result = 0
now = 1
for _ in range(int(sys.stdin.readline().rstrip())):
  next = int(sys.stdin.readline().rstrip())
  print('now, next', now, next)
  result += LCA(now, next)
  print(result)
  now = next
print(result)
print(level)
print(dp)