# [수 정렬하기 2]

import sys
n = int(input())
data = []
for i in range(n):
  data.append(int(sys.stdin.readline().rstrip()))
data.sort()
for i in data:
  print(i)