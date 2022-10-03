# [숫자 카드]
# 10815번
from bisect import bisect_left, bisect_right
def count_by_value(array, left, right):
  left = bisect_left(array, left)
  right = bisect_right(array, right)
  return right - left

import sys
n = int(sys.stdin.readline())
arrayA = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arrayB = list(map(int, sys.stdin.readline().rstrip().split()))

arrayA.sort()
for i in arrayB:
  if count_by_value(arrayA, i, i) != 0:
    print('1', end=' ')
  else:
    print('0', end=' ')