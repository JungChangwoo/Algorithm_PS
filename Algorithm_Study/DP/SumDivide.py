# [합분해]
# 2225번
import sys
def DFS(idx, value):
  global n, k, result, dp
  if value > n:
    return 0
    
  if idx == k:
    if value == n:
      dp[idx][value] = 1
    return dp[idx][value]
    
  if dp[idx][value] != 0:
    return dp[idx][value]
  
  for i in range(n + 1):
    dp[idx][value] += DFS(idx + 1, value + i) % 1000000000
  return dp[idx][value]
    
n, k = map(int, sys.stdin.readline().split())
result = 0
dp = [[0] * ((n * k)+1) for _ in range(k+1)]
DFS(0, 0)
print(dp[0][0] % 1000000000)