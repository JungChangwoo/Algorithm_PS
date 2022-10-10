# [동전 0]
# 11047번
import sys
n, k = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
  data.append(int(sys.stdin.readline().rstrip()))

result = 0
for i in range(n-1, -1, -1):
  value = data[i]
  count = k // value
  k -= value * count
  result += count
  if k == 0:
    print(result)
    break
