# [수 찾기]
# 문제 번호: 1920

n = int(input())
arrayN = list(map(int, input().split()))
m = int(input())
arrayM = list(map(int, input().split()))

arrayN.sort()

from bisect import bisect_left, bisect_right
def count_by_value(array, left, right):
  left = bisect_left(array, left)
  right = bisect_right(array, right)
  return right - left
  
for i in arrayM:
  if count_by_value(arrayN, i, i) == 0:
    print(0)
  else:
    print(1)