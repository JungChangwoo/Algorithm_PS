# [가장 긴 증가하는 부분 수열 4]
# 14002번

import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if array[i] > array[j]:
      dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)

idx = dp.index(max_dp)
path = []
while idx >= 0:
  if dp[idx] == max_dp:
    path.append(array[idx])
    max_dp -= 1
  idx -= 1

path.reverse()
print(*path)