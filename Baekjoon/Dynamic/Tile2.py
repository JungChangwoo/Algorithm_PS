# [2xn 타일링 2]
# 11727번
import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
  dp[i] += dp[i-1]
  dp[i] += dp[i-2] * 2
print(dp[n] % 10007)