# [평범한 배낭]
# 12866번
import sys

n, k = map(int, sys.stdin.readline().split())
d = [0] * (k + 1)

for i in range(n):
  w, v = map(int, sys.stdin.readline().split())
  for j in range(k, w-1, -1):
    d[j] = max(d[j], d[j-w] + v)
print(d[k])