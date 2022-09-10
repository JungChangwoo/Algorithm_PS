# [가장 긴 증가하는 부분 수열 3]
# 12738번

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
dp = [array[0]]

from bisect import bisect_left
for i in range(1, n):
    if array[i] > dp[-1]:
        dp.append(array[i])
    else:
        idx = bisect_left(dp, array[i])
        dp[idx] = array[i]
        print(dp)

print(len(dp))
