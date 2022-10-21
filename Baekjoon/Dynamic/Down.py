# [내려가기]
# 2096번
import sys
n = int(sys.stdin.readline().rstrip())

max_dp = [0] * 3
min_dp = [0] * 3

for i in range(n):
  values = list(map(int, sys.stdin.readline().split()))
  if i == 0:
    max_dp = values[:]
    min_dp = values[:]
    continue
  max_temp = max_dp[:]
  min_temp = min_dp[:]
  for j in range(3):
    max_dp[j] = max_temp[j] + values[j]
    min_dp[j] = min_temp[j] + values[j]
    if j - 1 >= 0:
      max_dp[j] = max(max_dp[j], max_temp[j-1] + values[j])
      min_dp[j] = min(min_dp[j], min_temp[j-1] + values[j])
    if j + 1 < 3:
      max_dp[j] = max(max_dp[j], max_temp[j+1] + values[j])
      min_dp[j] = min(min_dp[j], min_temp[j+1] + values[j])
print(max(max_dp), min(min_dp))