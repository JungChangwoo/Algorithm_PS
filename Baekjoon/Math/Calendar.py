# [카잉 달력]
# 6064번
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  m, n, x, y = map(int, sys.stdin.readline().split())
  
  x = x % (m+1)
  y = y % (n+1)
  while x <= m * n or y <= m * n:
    if x == y:
      print(x)
      break
    if x < y:
      x += m
    else:
      y += n
  if x > m * n or y > m * n:
    print(-1)
  