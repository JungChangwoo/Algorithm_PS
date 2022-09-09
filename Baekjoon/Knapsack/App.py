# [앱]
# 7579번
import sys
N, M = map(int, sys.stdin.readline().split())
m = [0] + list(map(int, sys.stdin.readline().split()))
c = [0] + list(map(int, sys.stdin.readline().split()))
INF = int(1e9)
dp = [[0] * (sum(c)+1) for _ in range(N+1)]

result = sum(c)

for i in range(1, N+1):
  byte = m[i]
  cost = c[i]
  for j in range(1, sum(c) + 1):
    if j < cost:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
    if dp[i][j] >= M:
      result = min(result, j)

if M != 0:
  print(result)
else:
  print(0)
