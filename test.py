import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
array = sorted(list(map(int, sys.stdin.readline().split())))
result = list(combinations_with_replacement(array, m))
result = set(result)
result = list(result)
result.sort()
for i in result:
  print(*i)