# [부녀회장이 될테야]
# 2775번
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  k = int(sys.stdin.readline().rstrip())
  n = int(sys.stdin.readline().rstrip())
  dp = [[i+1 for i in range(n)] for _ in range(k+1)]
  for f in range(k):
    value = 0
    for i in range(n):
      value += dp[f][i]
      dp[f+1][i] = value
  print(dp[k][n-1])

  
    