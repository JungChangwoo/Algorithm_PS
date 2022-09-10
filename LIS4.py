# [가장 긴 증가하는 부분 수열 4]
# 14002번

import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
path = []
max_length = 0
for i in range(n):
  max_idx = -1
  for j in range(i):
    if array[i] > array[j]:
      if dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
        max_length 
        max_idx = j
  
  

print(dp[-1])
print(path)