# [패션왕 신해빈]
# 9375번
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  n = int(sys.stdin.readline().rstrip())
  dict = {}
  for _ in range(n):
    name, category = sys.stdin.readline().split()
    if category in dict:
      dict[category] += 1
    else:
      dict[category] = 1
  result = 1
  for count in list(dict.values()):
    result *= (count + 1)
  print(result - 1)
    