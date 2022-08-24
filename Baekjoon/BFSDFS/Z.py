# [Z]
# 1074번

import sys
n, r, c = map(int, sys.stdin.readline().split())

# 4등분
import math
def get(n, x, y, value):
  # 마지막 도착
  if n == 1:
    nx = x % 2
    ny = y % 2
    if nx == 0 and ny == 0:
      return value
    if nx == 0 and ny == 1:
      return value + 1
    if nx == 1 and ny == 0:
      return value + 2
    if nx == 1 and ny == 1:
      return value + 3

  nx = x // math.pow(2, n-1)
  ny = y // math.pow(2, n-1)
  # 왼쪽위
  if nx == 0 and ny == 0:
    return get(n-1, x, y, value + math.pow(4, n-1) * 0)
  # 오른쪽위
  if nx == 0 and ny == 1:
    return get(n-1, x, y - math.pow(2, n-1), value + math.pow(4, n-1) * 1)
  # 왼쪽아래
  if nx == 1 and ny == 0:
    return get(n-1, x - math.pow(2, n-1), y, value + math.pow(4, n-1) * 2)
  # 오른쪽아래
  if nx == 1 and ny == 1:
    return get(n-1, x-math.pow(2, n-1), y-math.pow(2, n-1), value + math.pow(4, n-1) * 3)
  
print(int(get(n, r, c, 0)))
