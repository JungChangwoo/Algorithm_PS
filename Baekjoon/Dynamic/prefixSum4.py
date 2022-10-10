# [구간 합 구하기 4]
# 11659번
import sys
n, m = map(int, sys.stdin.readline().split())
array = [0] + list(map(int, sys.stdin.readline().split()))

total = 0
for i in range(1, n+1):
  total += array[i]
  array[i] = total

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(array[b] - array[a-1])
