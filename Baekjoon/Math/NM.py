# [N과 M (4)]
# 15652번
import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
array = [i for i in range(1, n+1)]
result = list(combinations_with_replacement(array, m))
for comb in result:
  print(*comb)

# [N과 M (8)]
# 15657번
import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = list(combinations_with_replacement(array, m))
for i in range(len(result)):
  result[i] = list(result[i])
  result[i].sort()
result.sort()
for comb in result:
  print(*comb)
# 직접구현
n, m = map(int, sys.stdin.readline().split())
array = sorted(list(map(int, sys.stdin.readline().split())))

temp = []
def DFS(start):
  if len(temp) == m:
    print(*temp)
    return
  for i in range(start, n):
    temp.append(array[i])
    DFS(i)
    temp.pop()
DFS(0)

# [N과 M (9)]
# 15663번
import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = list(combinations_with_replacement(array, m))
for i in range(len(result)):
  result[i] = list(result[i])
  result[i].sort()
result.sort()
for comb in result:
  print(*comb)

# [N과 M (12)]
# 15666번
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