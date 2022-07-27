# [ATM]
# 문제 번호: 11399

import sys
n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

data.sort()
result = 0
value = data[0]
result += value
for i in range(1, n):
  value += data[i]
  result += value

print(result)