# [신입사원]
# 1946번
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  array.sort()
  result = 0
  min_value = int(1e9)
  for a, b in array:
    if b < min_value:
      min_value = b
      result += 1
  print(result)