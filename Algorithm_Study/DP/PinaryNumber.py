# [이친수]
# 2193번
import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * n
dp[0] = 1

for i in range(1, n):
  dp[i] = dp[i-2] + dp[i-1]
print(dp[-1])