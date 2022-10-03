# [가장 긴 증가하는 부분 수열 5]
# 14003번

import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
dp = [array[0]]
dp_index = [1 for _ in range(n)]

from bisect import bisect_left
for i in range(1, n):
    if array[i] > dp[-1]:
        dp.append(array[i])
        dp_index[i] = len(dp)
    else:
        idx = bisect_left(dp, array[i])
        dp[idx] = array[i]
        dp_index[i] += idx

print(len(dp))
max_value = max(dp_index)
idx = dp_index.index(max_value)
path = []
while idx >= 0:
    if dp_index[idx] == max_value:
        max_value -= 1
        path.append(array[idx])
    idx -= 1
path.reverse()
print(*path)
