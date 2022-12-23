# [요세푸스 문제 0]
# 11866번
import sys
n, k = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, n+1)]
idx = k-1
result = []
while arr:
  idx %= len(arr)
  result.append(arr.pop(idx))
  idx += k - 1
print('<'+', '.join(str(s) for s in result)+'>')