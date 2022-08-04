# [시험 감독]
# 13458
import math
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b,c = map(int, sys.stdin.readline().rstrip().split())

result = 0
for i in a:
  i = i - b
  result += 1
  if i > 0:
    result += math.ceil(i / c)

print(result)