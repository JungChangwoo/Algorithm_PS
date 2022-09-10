# [가장 긴 증가하는 부분 수열 3]
# 12738번

import sys
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
dp = [1]
x = [array[0]] 

from bisect import bisect_left
for i in range(1, n):
    if array[i] > x[-1]:
        dp.append(dp[-1] + 1)
        x.append(array[i])
    else:
        idx = bisect_left(x, array[i])
        x[idx] = array[i]

print(dp[-1])
  