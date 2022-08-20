# [N과 M 5]
# 15654번

from itertools import permutations
import sys
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array.sort()
result = list(permutations(array, m))
for res in result:
  for j in res:
    print(j, end=' ')
  print()
