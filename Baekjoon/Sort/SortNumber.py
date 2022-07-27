# [수 정렬하기]
# 문제 번호: 2750

import sys
n = int(input())
data = []
for i in range(n):
  data.append(int(sys.stdin.readline().rstrip()))

data.sort()
for i in range(n):
  print(data[i])