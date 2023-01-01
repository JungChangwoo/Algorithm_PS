# [최소공배수]
# 1934
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  a, b = map(int, sys.stdin.readline().split())
  value = max(a, b)
  temp = value
  count = 1
  while temp < (a * b) + 1:
    temp = value * count
    if temp % a == 0 and temp % b == 0:
      print(temp)
      break
    count += 1