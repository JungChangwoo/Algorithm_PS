# [N과 M 2]
# 15650번
from itertools import combinations
import sys
n, m = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n+1)]
result = list(combinations(data, m))
for res in result:
  for j in res:
    print(j, end=' ')
  print()